from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CSVUploadSerializer
import logging
import pandas as pd
from .tasks import process_csv

logger = logging.getLogger(__name__)

class CSVUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            csv_file = serializer.validated_data['csv_file']
            df = pd.read_csv(csv_file, header=0)
            process_csv.delay(df)
            logger.info("CSV recebido")
            return Response({'message': 'Upload de CSV bem-sucedido.'})
        else:
            logger.error("Arquivo não encontrado ou inválido")
            return Response(serializer.errors, status=400)
