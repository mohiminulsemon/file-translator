# # translator/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import TranslatedFileSerializer
# from .models import TranslatedFile
# import googletrans
# import openpyxl
# from pptx import Presentation
# from django.core.files.base import ContentFile


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated  # Add permission check
# from .serializers import TranslatedFileSerializer
# from .models import TranslatedFile
# import googletrans
# import openpyxl
# from pptx import Presentation
# from django.core.files.base import ContentFile

# class TranslateFileView(APIView):
#     permission_classes = [IsAuthenticated]  # Require authentication for file uploads

#     def post(self, request):
#         serializer = TranslatedFileSerializer(data=request.data)
#         if serializer.is_valid():
#             original_file = serializer.validated_data['original_file']
#             target_language = serializer.validated_data['target_language']

#             # Determine file type and call appropriate translation function
#             file_extension = original_file.name.split('.')[-1].lower()
#             if file_extension == 'xlsx':
#                 translated_file_path = translate_xlsx(original_file.path, target_language)
#             elif file_extension == 'pptx':
#                 translated_file_path = translate_pptx(original_file.path, target_language)
#             else:
#                 return Response({'error': 'Unsupported file type'}, status=400)

#             # Save translated file to model
#             with open(translated_file_path, 'rb') as f:
#                 translated_file = ContentFile(f.read())
#             translated_file_instance = TranslatedFile.objects.create(
#                 original_file=original_file,
#                 translated_file=translated_file,
#                 target_language=target_language,
#                 user=request.user  # Associate translated file with the user
#             )
#             return Response({'id': translated_file_instance.id})
#         else:
#             return Response(serializer.errors, status=400)




# from pptx import Presentation
# from googletrans import Translator

# def translate_and_preserve_formatting(prs, target_language):
#     formatted_text_data = []
#     for slide in prs.slides:
#         for shape in slide.shapes:
#             if shape.has_text_frame:
#                 text = shape.text.text
#                 font = shape.text.font.name
#                 size = shape.text.font.size
#                 color = shape.text.font.color.rgb
#                 formatted_text_data.append({
#                     'text': text,
#                     'font': font,
#                     'size': size,
#                     'color': color
#                 })

#     translator = Translator()
#     translated_text_data = []
#     for item in formatted_text_data:
#         translated_text = translator.translate(item['text'], dest=target_language).text
#         translated_text_data.append({
#             'text': translated_text,
#             'font': item['font'],
#             'size': item['size'],
#             'color': item['color']
#         })

#     i = 0
#     for slide in prs.slides:
#         for shape in slide.shapes:
#             if shape.has_text_frame:
#                 shape.text.text = translated_text_data[i]['text']
#                 shape.text.font.name = translated_text_data[i]['font']
#                 shape.text.font.size = Pt(translated_text_data[i]['size'])
#                 shape.text.font.color.rgb = translated_text_data[i]['color']
#                 i += 1


# import openpyxl
# from googletrans import Translator

# def translate_xlsx(file_path, target_language):
#     workbook = openpyxl.load_workbook(file_path)
#     translator = Translator()

#     for sheet in workbook.worksheets:
#         for row in sheet.iter_rows():
#             for cell in row:
#                 if cell.value is not None:
#                     translated_text = translator.translate(cell.value, dest=target_language).text
#                     cell.value = translated_text

#     workbook.save('translated_file.xlsx')  # Replace with desired filename


# from pptx import Presentation
# from googletrans import Translator

# def translate_pptx(file_path, target_language):
#     prs = Presentation(file_path)
#     translate_and_preserve_formatting(prs, target_language)  # Call the function here
#     prs.save('translated_file.pptx')



# from django.shortcuts import get_object_or_404
# from django.http import FileResponse, Http404
# from django.core.exceptions import PermissionDenied

# def download_translated_file(request, file_id):
#     try:
#         translated_file = get_object_or_404(TranslatedFile, id=file_id)
#         if not translated_file.translated_file:
#             raise Http404("Translated file not available for download.")

#         # Ensure user has permission to download the file (add your logic here)
#         if not request.user.has_perm('translation.download_translated_file'):  # Example permission check
#             raise PermissionDenied("You don't have permission to download this file.")

#         with open(translated_file.translated_file.path, 'rb') as f:
#             filename = translated_file.original_file.name  # Use original filename for better clarity
#             response = FileResponse(f, as_attachment=True)
#             response['Content-Disposition'] = f'attachment; filename="{filename}"'
#             return response

#     except (FileNotFoundError, PermissionError) as e:
#         # Handle potential file system errors or permission issues
#         return Response({'error': str(e)}, status=500)
