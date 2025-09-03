from pydantic import BaseModel

class InvoiceRequest(BaseModel):
    invoice_id: str
    amount: float
    due_date: str

class InvoiceResponse(BaseModel):
    invoice_id: str
    amount: float
    due_date: str
    paid: bool
