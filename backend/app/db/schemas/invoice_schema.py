from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class InvoiceSchema(BaseModel):
    invoice_id: int
    customer_id: int
    invoice_date: datetime
    billing_address: Optional[str] = None
    billing_city: Optional[str] = None
    billing_state: Optional[str] = None
    billing_country: Optional[str] = None
    billing_postal_code: Optional[str] = None
    total: Decimal

    class Config:
        from_attributes = True
