from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import SessionLocal
from app.db.models.customer import Customer
from app.db.schemas.customer_schema import CustomerSchema
from app.services.customer_service import CustomerService
from app.utils.response import format_response_with_headers

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.get("/customers")
async def get_customers(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(Customer)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(Customer).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Customer)
    response["total"] = total
    return response


@router.get("/customers/search")
async def search_customers(
    first_name: str | None = Query(None),
    email: str | None = Query(None),
    country: str | None = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Customer)

    if first_name:
        stmt = stmt.where(Customer.first_name.ilike(f"%{first_name}%"))
    if email:
        stmt = stmt.where(Customer.email.ilike(f"%{email}%"))
    if country:
        stmt = stmt.where(Customer.country.ilike(f"%{country}%"))

    # Total count
    total_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    # Paginated data
    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()

    response = format_response_with_headers(rows, Customer)
    response["total"] = total
    return response


@router.get("/customers/{customer_id}", response_model=CustomerSchema)
async def get_customer_by_id(customer_id: int, db: AsyncSession = Depends(get_db)):
    service = CustomerService(db)
    try:
        return await service.get_customer_by_id(customer_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Customer not found")
