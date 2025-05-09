from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import SessionLocal
from app.db.models.invoice_line import InvoiceLine
from app.db.schemas.invoice_line_schema import InvoiceLineSchema
from app.services.invoice_line_service import InvoiceLineService
from app.utils.response import format_response_with_headers

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.get("/invoice-lines")
async def get_invoice_lines(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(InvoiceLine)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(InvoiceLine).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, InvoiceLine)
    response["total"] = total
    return response


@router.get("/invoice-lines/search")
async def search_invoice_lines(
    invoice_id: int | None = Query(None),
    track_id: int | None = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(InvoiceLine)

    if invoice_id:
        stmt = stmt.where(InvoiceLine.invoice_id == invoice_id)
    if track_id:
        stmt = stmt.where(InvoiceLine.track_id == track_id)

    total_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()

    response = format_response_with_headers(rows, InvoiceLine)
    response["total"] = total
    return response


@router.get("/invoice-lines/{invoice_line_id}", response_model=InvoiceLineSchema)
async def get_invoice_line_by_id(invoice_line_id: int, db: AsyncSession = Depends(get_db)):
    service = InvoiceLineService(db)
    try:
        return await service.get_invoice_line_by_id(invoice_line_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Invoice line not found")
