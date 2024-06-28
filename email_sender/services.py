import logging
from .interfaces import EmailSender

logger = logging.getLogger(__name__)

class SimpleEmailSender(EmailSender):
    def send_email(self, data, email):
        def validate_email(email):
            pass
        logger.info(f"E-mail enviado com sucesso para {email} com o boleto: {data}")
        return validate_email(email)