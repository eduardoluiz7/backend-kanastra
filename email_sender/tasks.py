from .services import SimpleEmailSender
from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from debts.models import Debt
import logging


logger = logging.getLogger(__name__)

@shared_task
def send_invoice_emails():
    debts = Debt.objects.filter(status="PROCESSED", due_date__lte=date_limit)
    sender = SimpleEmailSender()
    today = timezone.now().date()
    date_limit = today + timedelta(days=10)

    for debt in debts:
        sent = sender.send_email(debt, debt.email)
        if not sent:
            logger.error(f"Erro ao enviar boleto via email para {debt.email}")
            continue
        logger.info(f"Boleto enviado para {debt.email}")
        debt.status = "CONFIRMED"
        debt.save()
        
