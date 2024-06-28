import logging
from .interfaces import InvoiceGenerator

logger = logging.getLogger(__name__)

class SimpleInvoiceGenerator(InvoiceGenerator):
    def generate_invoice(self, data):
        if not data:
            return False
        logger.info(f"Boleto gerado com sucesso para os dados: {data}")
        return True