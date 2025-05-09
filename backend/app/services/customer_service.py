from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Customer


class CustomerService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_customers(self):
        result = await self.db.execute(select(Customer))
        return result.scalars().all()

    async def get_customer_by_id(self, customer_id: int):
        result = await self.db.execute(select(Customer).where(Customer.customer_id == customer_id))
        customer = result.scalar_one_or_none()
        if customer is None:
            raise NoResultFound(f"Customer ID {customer_id} not found")
        return customer

    async def search_customers(self, first_name=None, email=None, country=None):
        stmt = select(Customer)

        if first_name:
            stmt = stmt.where(Customer.first_name.ilike(f"%{first_name}%"))
        if email:
            stmt = stmt.where(Customer.email.ilike(f"%{email}%"))
        if country:
            stmt = stmt.where(Customer.country.ilike(f"%{country}%"))

        result = await self.db.execute(stmt)
        return result.scalars().all()