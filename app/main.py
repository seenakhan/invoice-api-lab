from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from invoice_processor import Invoice

app = FastAPI()

# In-memory store for demo purposes
invoices = {}

class InvoiceRequest(BaseModel):
    invoice_id: str
    amount: float
    due_date: str

@app.post("/invoice/")
def create_invoice(data: InvoiceRequest):
    if data.invoice_id in invoices:
        raise HTTPException(status_code=400, detail="Invoice already exists.")
    invoice = Invoice(data.invoice_id, data.amount, data.due_date)
    invoices[data.invoice_id] = invoice
    return invoice.to_dict()

@app.get("/invoice/{invoice_id}")
def get_invoice(invoice_id: str):
    invoice = invoices.get(invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found.")
    return invoice.to_dict()

@app.post("/invoice/{invoice_id}/pay")
def pay_invoice(invoice_id: str):
    invoice = invoices.get(invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found.")
    invoice.mark_paid()
    return {"message": "Invoice marked as paid."}

@app.post("/invoice/{invoice_id}/late-fee")
def apply_late_fee(invoice_id: str):
    invoice = invoices.get(invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found.")
    invoice.apply_late_fee()
    return {"new_amount": invoice.amount}
