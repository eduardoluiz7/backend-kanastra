
from .models import Debt
from django.db import transaction
from django_rq import job
import logging
from email_sender.services import SimpleEmailSender


logger = logging.getLogger(__name__)

@job
def process_csv(dataframe):
    dataframe.columns = ["name", "government_id", "email", "debt_amount", "debt_due_date", "debt_id"]
    data_dict = dataframe.to_dict('records')
    for row in data_dict:
        process_row(row)


@transaction.atomic
def process_row(row):
    if not Debt.objects.filter(debt_id=row["debt_id"]).exists():
        new_invoice = Debt(**row)
        new_invoice.save()

