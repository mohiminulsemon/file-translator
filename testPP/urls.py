from django.urls import path
from .views import FileTranslateView

urlpatterns = [
    path('file-translate/', FileTranslateView.as_view(), name='file-translate'),
]
