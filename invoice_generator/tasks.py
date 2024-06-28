from invoice_generator.services import SimpleInvoiceGenerator
from debts.models import Debt
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def generate_invoices():
    generator = SimpleInvoiceGenerator()
    invoices = Debt.objects.filter(status="PENDING")

    for inv in invoices:
        gen = generator.generate_invoice(inv.name)
        if not gen:
           logger.error(f"Erro ao gerar boleto da divida {inv.id}")
        inv.status = "PROCESSED"
        inv.save()
        logger.info(f"Boleto gerado para a divida {inv.id}")