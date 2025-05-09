from pydantic import BaseModel


class CustomerSchema(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    company: str | None = None
    address: str
    city: str
    state: str | None = None
    country: str
    postal_code: str | None = None
    phone: str | None = None
    fax: str | None = None
    email: str
    support_rep_id: int

    class Config:
        from_attributes = True
