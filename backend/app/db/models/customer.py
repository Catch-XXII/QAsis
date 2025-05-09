from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column("customer_id", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    company = Column("company", String, nullable=True)
    address = Column("address", String)
    city = Column("city", String)
    state = Column("state", String, nullable=True)
    country = Column("country", String)
    postal_code = Column("postal_code", String)
    phone = Column("phone", String)
    fax = Column("fax", String, nullable=True)
    email = Column("email", String)
    support_rep_id = Column("support_rep_id", Integer)
