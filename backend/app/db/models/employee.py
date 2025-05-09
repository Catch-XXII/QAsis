from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.db.database import Base


class Employee(Base):
    __tablename__ = "employee"

    employee_id = Column("employee_id", Integer, primary_key=True)
    last_name = Column("last_name", String, nullable=False)
    first_name = Column("first_name", String, nullable=False)
    title = Column("title", String, nullable=True)
    reports_to = Column("reports_to", Integer, ForeignKey("employee.employee_id"), nullable=True)
    birth_date = Column("birth_date", DateTime, nullable=True)
    hire_date = Column("hire_date", DateTime, nullable=True)
    address = Column("address", String, nullable=True)
    city = Column("city", String, nullable=True)
    state = Column("state", String, nullable=True)
    country = Column("country", String, nullable=True)
    postal_code = Column("postal_code", String, nullable=True)
    phone = Column("phone", String, nullable=True)
    fax = Column("fax", String, nullable=True)
    email = Column("email", String, nullable=True)
