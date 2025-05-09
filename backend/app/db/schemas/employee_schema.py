from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EmployeeSchema(BaseModel):
    employee_id: int
    last_name: str
    first_name: str
    title: Optional[str] = None
    reports_to: Optional[int] = None
    birth_date: Optional[datetime] = None
    hire_date: Optional[datetime] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None

    class Config:
        from_attributes = True
