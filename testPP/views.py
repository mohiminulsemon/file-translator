from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import TranslatedFile, FileModel
from .serializers import TranslatedFileSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from .serializers import FileSerializer
from django.core.files.base import ContentFile
import os

class FileTranslateView(APIView):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        
        if serializer.is_valid():
            text = serializer.validated_data['text']
            # Save the model instance first to obtain the actual file path
            file_model = serializer.save()

            # Access the saved file object for modifications
            file_object = file_model.file

            # Temporarily save the file to disk for modification
            with open('temporary_file.txt', 'wb') as f:
                for chunk in file_object.chunks():
                    f.write(chunk)

            # Perform text replacement on the temporary file
            with open('temporary_file.txt', 'r') as f:
                file_contents = f.read()
            modified_contents = file_contents.replace(text, "hello this is new text")  # Replace with your actual logic

            # Create a new file object with modified contents
            new_file_object = ContentFile(modified_contents, name=file_object.name)

            # Update the model instance with the new file object
            file_model.file.save(new_file_object.name, new_file_object)
            file_model.save()

            # Generate download URL for the updated file
            download_url = file_object.url  # URL points to the updated file

            return Response({'download_url': download_url})
        else:
            return Response(serializer.errors, status=400)

        


class TranslatedFileViewSet(viewsets.ModelViewSet):
    queryset = TranslatedFile.objects.all()
    serializer_class = TranslatedFileSerializer

    @action(detail=False, methods=['post'])
    def upload_and_translate(self, request):
        file_serializer = TranslatedFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

            # Read the uploaded file and replace text
            translated_file = file_serializer.instance
            new_text = request.data.get('text', 'hello this is new text')

            file_path = translated_file.file.path
            with open(file_path, 'r') as file:
                content = file.read()
                content = content.replace(translated_file.text, new_text)

            # Write the updated content to the file
            with open(file_path, 'w') as file:
                file.write(content)

            # Update the model instance
            translated_file.text = new_text
            translated_file.save()

            return Response(
                {'detail': 'File uploaded and text replaced successfully',
                 'download_url': translated_file.translated_file.url},
                status=status.HTTP_201_CREATED
            )

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
