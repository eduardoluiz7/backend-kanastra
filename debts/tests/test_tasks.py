from django.test import TestCase
from debts.models import Debt 
from debts.tasks import process_row 

class ProcessRowTest(TestCase):
    def setUp(self):
        self.existing_row = {
            "debt_id": 1,
            "debt_amount": 100,
            "name": "Existing debt"
        }
        self.new_row = {
            "debt_id": 2,
            "debt_amount": 200,
            "name": "New debt"
        }
        Debt.objects.create(**self.existing_row)

    def test_process_row_creates_new_debt(self):
        self.assertFalse(Debt.objects.filter(debt_id=self.new_row["debt_id"]).exists())
        
        process_row(self.new_row)
        
        self.assertTrue(Debt.objects.filter(debt_id=self.new_row["debt_id"]).exists())
        
        new_debt = Debt.objects.get(debt_id=self.new_row["debt_id"])
        self.assertEqual(new_debt.debt_amount, self.new_row["debt_amount"])
        self.assertEqual(new_debt.name, self.new_row["name"])

    def test_process_row_does_not_create_existing_debt(self):
        self.assertTrue(Debt.objects.filter(debt_id=self.existing_row["debt_id"]).exists())
        
        process_row(self.existing_row)
        
        debts = Debt.objects.filter(debt_id=self.existing_row["debt_id"])
        self.assertEqual(debts.count(), 1)
        
        existing_debt = debts.first()
        self.assertEqual(existing_debt.debt_amount, self.existing_row["debt_amount"])
        self.assertEqual(existing_debt.name, self.existing_row["name"])