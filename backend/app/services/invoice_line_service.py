from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.invoice_line import InvoiceLine


class InvoiceLineService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_invoice_lines(self):
        result = await self.db.execute(select(InvoiceLine))
        return result.scalars().all()

    async def get_invoice_line_by_id(self, invoice_line_id: int):
        result = await self.db.execute(select(InvoiceLine).where(InvoiceLine.invoice_line_id == invoice_line_id))
        invoice_line = result.scalar_one_or_none()
        if invoice_line is None:
            raise NoResultFound(f"InvoiceLine ID {invoice_line_id} not found")
        return invoice_line

    async def search_invoice_lines(self, invoice_id=None, track_id=None):
        stmt = select(InvoiceLine)
        if invoice_id:
            stmt = stmt.where(InvoiceLine.invoice_id == invoice_id)
        if track_id:
            stmt = stmt.where(InvoiceLine.track_id == track_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()