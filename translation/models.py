# translator/models.py
from django.db import models
from django.contrib.auth.models import User  # For user association

class TranslatedFile(models.Model):
    original_file = models.FileField(upload_to='original_files/')
    translated_file = models.FileField(upload_to='translated_files/', blank=True, null=True)
    target_language = models.CharField(max_length=50)

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
