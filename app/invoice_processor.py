from datetime import datetime
import json
import logging

class Invoice:
    def __init__(self, invoice_id, amount, due_date):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.paid = False

    def mark_paid(self):
        self.paid = True
        logging.info(f"Invoice {self.invoice_id} marked as paid.")

    def is_overdue(self, reference_date=None):
        ref = reference_date or datetime.now()
        return ref > self.due_date and not self.paid

    def apply_late_fee(self):
        if self.is_overdue():
            self.amount = round(self.amount * 1.05, 2)

    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "amount": self.amount,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "paid": self.paid
        }
