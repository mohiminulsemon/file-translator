from django.db import models

class TranslatedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    text = models.TextField()
    translated_file = models.FileField(upload_to='translated/')


class FileModel(models.Model):
    file = models.FileField(upload_to='uploaded_files/')  # Adjust upload path as needed
    text = models.CharField(max_length=255 , blank=True, null=True)