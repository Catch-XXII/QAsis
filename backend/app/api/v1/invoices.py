from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import SessionLocal
from app.db.models.invoice import Invoice
from app.db.schemas.invoice_schema import InvoiceSchema
from app.services.invoice_service import InvoiceService
from app.utils.response import format_response_with_headers

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.get("/invoices")
async def get_invoices(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(Invoice)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(Invoice).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Invoice)
    response["total"] = total
    return response


@router.get("/invoices/search")
async def search_invoices(
    customer_id: int | None = Query(None),
    billing_country: str | None = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Invoice)

    if customer_id:
        stmt = stmt.where(Invoice.customer_id == customer_id)
    if billing_country:
        stmt = stmt.where(Invoice.billing_country.ilike(f"%{billing_country}%"))

    total_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()

    response = format_response_with_headers(rows, Invoice)
    response["total"] = total
    return response


@router.get("/invoices/{invoice_id}", response_model=InvoiceSchema)
async def get_invoice_by_id(invoice_id: int, db: AsyncSession = Depends(get_db)):
    service = InvoiceService(db)
    try:
        return await service.get_invoice_by_id(invoice_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Invoice not found")
