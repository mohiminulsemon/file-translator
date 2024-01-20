# translator/models.py
from django.db import models
from django.contrib.auth.models import User  # For user association

class TranslatedFile(models.Model):
    original_file = models.FileField(upload_to='original_files/')
    translated_file = models.FileField(upload_to='translated_files/', blank=True, null=True)
    target_language = models.CharField(max_length=50)

