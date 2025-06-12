from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import io

class TextUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')
        
        if not uploaded_file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not uploaded_file.name.endswith('.txt'):
            return Response({'error': 'Only .txt files are allowed'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            content = uploaded_file.read().decode('utf-8')
            word_count = len(content.split())
            return Response({'word_count': word_count}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
