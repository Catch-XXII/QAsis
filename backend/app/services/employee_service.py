from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.employee import Employee


class EmployeeService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_employees(self):
        result = await self.db.execute(select(Employee))
        return result.scalars().all()

    async def search_employees(self, last_name=None, title=None, country=None):
        stmt = select(Employee)
        if last_name:
            stmt = stmt.where(Employee.last_name.ilike(f"%{last_name}%"))
        if title:
            stmt = stmt.where(Employee.title.ilike(f"%{title}%"))
        if country:
            stmt = stmt.where(Employee.country.ilike(f"%{country}%"))
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_employee_by_id(self, employee_id: int):
        result = await self.db.execute(select(Employee).where(Employee.employee_id == employee_id))
        employee = result.scalar_one_or_none()
        if employee is None:
            raise NoResultFound(f"Employee ID {employee_id} not found")
        return employee

