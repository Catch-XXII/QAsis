from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String

from app.db.database import Base


class Invoice(Base):
    __tablename__ = "invoice"

    invoice_id = Column("invoice_id", Integer, primary_key=True)
    customer_id = Column("customer_id", Integer, ForeignKey("customer.customer_id"), nullable=False)
    invoice_date = Column("invoice_date", DateTime, nullable=False)
    billing_address = Column("billing_address", String, nullable=True)
    billing_city = Column("billing_city", String, nullable=True)
    billing_state = Column("billing_state", String, nullable=True)
    billing_country = Column("billing_country", String, nullable=True)
    billing_postal_code = Column("billing_postal_code", String, nullable=True)
    total = Column("total", Numeric, nullable=False)
