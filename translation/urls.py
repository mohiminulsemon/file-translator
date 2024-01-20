from django.urls import path
from . import views

app_name = 'translation'  # Naming the app for URL namespace

urlpatterns = [
    path('', views.TranslateFileView.as_view(), name='translate_file'),  # Upload and translate file
    path('download/<int:file_id>/', views.download_translated_file, name='download_translated_file'),  # Download translated file
]
