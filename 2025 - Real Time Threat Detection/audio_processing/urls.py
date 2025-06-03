from django.urls import path
from .views import record_page, start_listening, stop_listening, stream_audio
from django.http import JsonResponse
from django.views.generic import TemplateView

urlpatterns = [
    path('', record_page, name='record'),
    path('start/', start_listening, name='start-listening'),
    path('stop/', stop_listening, name='stop-listening'),
    path('stream/', stream_audio, name='stream-audio'),
    path('projects/', lambda request: JsonResponse({'message': 'Projects API works!'})),
    path('test-audio/', TemplateView.as_view(template_name='test_audio.html'), name='test-audio'),
]
