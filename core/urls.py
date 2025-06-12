from django.urls import path
from .views import TextUploadView

urlpatterns = [
    path('upload/', TextUploadView.as_view(), name='text-upload'),
]
