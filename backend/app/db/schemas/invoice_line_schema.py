from decimal import Decimal

from pydantic import BaseModel


class InvoiceLineSchema(BaseModel):
    invoice_line_id: int
    invoice_id: int
    track_id: int
    unit_price: Decimal
    quantity: int

    class Config:
        from_attributes = True
