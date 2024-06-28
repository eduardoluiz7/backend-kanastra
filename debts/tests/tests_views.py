import io
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch

class CSVUploadViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api/upload-csv')

    def test_csv_upload_success(self):
        csv_content = io.StringIO("col1,col2\nvalue1,value2\nvalue3,value4")
        csv_file = io.BytesIO(csv_content.getvalue().encode('utf-8'))
        csv_file.name = 'test.csv'

        with patch('caminho.para.sua.process_csv.delay') as mock_process_csv:
            response = self.client.post(self.url, {'csv_file': csv_file}, format='multipart')

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['message'], 'Upload de CSV bem-sucedido.')
            mock_process_csv.assert_called_once()

    def test_csv_upload_invalid_file(self):
        response = self.client.post(self.url, {'csv_file': ''}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('csv_file', response.data)