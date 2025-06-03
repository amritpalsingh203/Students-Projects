from django.contrib import admin
from django.urls import path, include
from audio_processing.views import record_page # Import your views
from RealtimeSTT import AudioToTextRecorder

# At the top, only once:
realtime_stt = AudioToTextRecorder(
    model="tiny",
    device="cpu",
    compute_type="float32",
    batch_size=1,
    language="en",
)

def process_audio_chunk(chunk):
    ...
    result = realtime_stt.transcribe(chunk)
    ...

urlpatterns = [
    path("admin/", admin.site.urls),  # Django admin panel
    path("", record_page, name="home"), 
     # Default recording page
    path("api/", include("audio_processing.urls")),
]
