from rest_framework import serializers
from .models import TranslatedFile , FileModel

class TranslatedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatedFile
        fields = ['id', 'file', 'text', 'translated_file']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel  # Specify the model to serialize
        fields = ('id','file', 'text')  # Include both fields