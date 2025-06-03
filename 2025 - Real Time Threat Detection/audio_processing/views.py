import os
import json
import wave
from django.conf import settings
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rapidfuzz import fuzz
import subprocess
from pydub import AudioSegment
import torch
import librosa
from RealtimeSTT import AudioToTextRecorder
import numpy as np
import queue
import threading
import time
import scipy.signal

# Ensure media directory exists
MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

# Initialize RealtimeSTT
device = "cuda:0" if torch.cuda.is_available() else "cpu"
realtime_stt = AudioToTextRecorder(
    model="tiny",
    device="cpu",
    compute_type="float32",
    batch_size=1,
    language="en",
)

# Define words associated with threats
THREAT_WORDS = ["bomb", "attack", "shoot", "kill", "threat", "danger", "terrorist"]

# Global queue for audio chunks
audio_queue = queue.Queue()
is_listening = False

AUDIO_BUFFER = []
BUFFER_SIZE = 16000  # 1 second at 16kHz

def record_page(request):
    """ Render the recording UI """
    return render(request, 'record.html')

def process_audio_chunk(chunk):
    global AUDIO_BUFFER
    AUDIO_BUFFER.extend(chunk.tolist())
    print(f"[Backend] Buffer length: {len(AUDIO_BUFFER)}")
    if len(AUDIO_BUFFER) < BUFFER_SIZE:
        return None  # Not enough audio yet

    # Process the buffer
    audio_to_process = np.array(AUDIO_BUFFER[:BUFFER_SIZE], dtype=np.float32)
    AUDIO_BUFFER = AUDIO_BUFFER[BUFFER_SIZE:]  # Remove processed samples

    try:
        print("[Backend] Instantiating model and feeding buffered audio...")
        result = AudioToTextRecorder(
            model="tiny",
            device="cpu",
            compute_type="float32",
            batch_size=2
        )
        result.feed_audio(audio_to_process)
        text = result.text()
        print("[Backend] Transcription result:", text)
        if result and text:
            is_threat = any(word in text.lower() for word in THREAT_WORDS)
            print("[Backend] Threat detected:" if is_threat else "[Backend] No threat detected.")
            return {
                "text": text,
                "is_threat": is_threat,
                "threat_words": [word for word in THREAT_WORDS if word in text.lower()]
            }
    except Exception as e:
        print(f"[Backend] Error processing chunk: {str(e)}")
    return None

def audio_processor():
    """Background thread to process audio chunks"""
    print("[Backend] Audio processor started. is_listening:", is_listening)
    while is_listening or not audio_queue.empty():
        try:
            if not audio_queue.empty():
                print("[Backend] Getting chunk from queue...")
                chunk = audio_queue.get()
                result = process_audio_chunk(chunk)
                if result:
                    print("[Backend] Yielding result to frontend:", result)
                    yield f"data: {json.dumps(result)}\n\n"
            time.sleep(0.1)  # Small delay to prevent CPU overload
        except Exception as e:
            print(f"[Backend] Error in audio processor: {str(e)}")

@csrf_exempt
def start_listening(request):
    """Start the real-time listening process"""
    global is_listening
    is_listening = True
    
    def event_stream():
        try:
            for result in audio_processor():
                yield result
        finally:
            is_listening = False
    
    return StreamingHttpResponse(
        event_stream(),
        content_type='text/event-stream'
    )

@csrf_exempt
def stop_listening(request):
    """Stop the real-time listening process"""
    global is_listening
    is_listening = False
    return JsonResponse({"status": "stopped"})

@csrf_exempt
def stream_audio(request):
    """Handle incoming audio stream chunks"""
    if request.method == "POST" and request.FILES.get("audio"):
        try:
            audio_file = request.FILES["audio"]
            print("[Backend] Received audio file of size:", audio_file.size)
            # Convert the audio chunk to numpy array
            audio_data = np.frombuffer(audio_file.read(), dtype=np.float32)
            print("[Backend] Converted audio to numpy array of shape:", audio_data.shape)
            # Add to processing queue
            audio_queue.put(audio_data)
            print("[Backend] Audio chunk added to queue.")
            return JsonResponse({"status": "received"})
        except Exception as e:
            print(f"[Backend] Error receiving audio chunk: {str(e)}")
            return JsonResponse({"error": str(e)}, status=400)
    print("[Backend] No audio data received in POST request.")
    return JsonResponse({"error": "No audio data received"}, status=400)