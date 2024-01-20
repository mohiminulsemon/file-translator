# translator/serializers.py
from rest_framework import serializers
from .models import TranslatedFile

class TranslatedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatedFile
        fields = ('id', 'original_file', 'target_language')  # Add 'user' if you want to expose it in API responses

    # Validation for file extension and size (from previous responses)
    def validate_original_file(self, value):
        allowed_extensions = ['.xlsx', '.pptx']
        if not value.name.lower().endswith(allowed_extensions):
            raise serializers.ValidationError('Unsupported file type. Allowed extensions are: {}'.format(', '.join(allowed_extensions)))
        max_size = 10485760  # 10 MB
        if value.size > max_size:
            raise serializers.ValidationError('File size exceeds maximum allowed size of {} bytes.'.format(max_size))
        return value
