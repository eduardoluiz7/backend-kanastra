from django.test import TestCase
from services import SimpleInvoiceGenerator
import logging

class SimpleInvoiceGeneratorTests(TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_generate_invoice_success(self):
        generator = SimpleInvoiceGenerator()

        with self.assertLogs('invoice_generator.service', level='INFO') as cm:
            generator.generate_invoice("123456")
            self.assertIn(f"Boleto gerado com sucesso para os dados: 123456", cm.output[0])
    
    def test_generate_invoice_fail(self):
        generator = SimpleInvoiceGenerator()

        result = generator.generate_invoice("789012", "another_user@example.com")
        self.assertFalse(result)