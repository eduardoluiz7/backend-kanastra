from django.test import TestCase
from services import SimpleEmailSender
import logging

class SimpleEmailSenderTests(TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)
    
    def test_send_email_success(self):
        sender = SimpleEmailSender()
        with self.assertLogs('email_sender.services', level='INFO') as cm:
            result = sender.send_email("123456", "user@example.com")
            self.assertTrue(result)
            self.assertIn(f"E-mail enviado com sucesso para user@example.com com o boleto: 123456", cm.output[0])

    def test_send_email_failure(self):
        sender = SimpleEmailSender()

        result = sender.send_email("789012", "another_user@example.com")
        self.assertFalse(result)