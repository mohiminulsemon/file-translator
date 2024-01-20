from django.urls import path
from . import views
from .views import UploadedFileListCreateView, FileListView, download_file 
app_name = 'translation'  # Naming the app for URL namespace

urlpatterns = [
    path('', views.TranslateFileView.as_view(), name='translate_file'),  # Upload and translate file
    path('download/<int:file_id>/', views.download_translated_file, name='download_translated_file'),  # Download translated file
    path('files/', UploadedFileListCreateView.as_view(), name='file-list-create'),
    path('file-list/', FileListView.as_view(), name='file-list'),
    path('file-download/<int:file_id>/', download_file, name='file-download'),
]
