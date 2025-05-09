from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.invoice import Invoice


class InvoiceService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_invoices(self):
        result = await self.db.execute(select(Invoice))
        return result.scalars().all()

    async def get_invoice_by_id(self, invoice_id: int):
        result = await self.db.execute(select(Invoice).where(Invoice.invoice_id == invoice_id))
        invoice = result.scalar_one_or_none()
        if invoice is None:
            raise NoResultFound(f"Invoice ID {invoice_id} not found")
        return invoice

    async def search_invoices(self, customer_id=None, billing_country=None):
        stmt = select(Invoice)
        if customer_id:
            stmt = stmt.where(Invoice.customer_id == customer_id)
        if billing_country:
            stmt = stmt.where(Invoice.billing_country.ilike(f"%{billing_country}%"))
        result = await self.db.execute(stmt)
        return result.scalars().all()