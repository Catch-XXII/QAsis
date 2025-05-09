from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import SessionLocal
from app.db.models.employee import Employee
from app.db.schemas.employee_schema import EmployeeSchema
from app.services.employee_service import EmployeeService
from app.utils.response import format_response_with_headers

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.get("/employees")
async def get_employees(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(Employee)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(Employee).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Employee)
    response["total"] = total
    return response


@router.get("/employees/search")
async def search_employees(
    last_name: str | None = Query(None),
    title: str | None = Query(None),
    country: str | None = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Employee)

    if last_name:
        stmt = stmt.where(Employee.last_name.ilike(f"%{last_name}%"))
    if title:
        stmt = stmt.where(Employee.title.ilike(f"%{title}%"))
    if country:
        stmt = stmt.where(Employee.country.ilike(f"%{country}%"))

    total_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()

    response = format_response_with_headers(rows, Employee)
    response["total"] = total
    return response


@router.get("/employees/{employee_id}", response_model=EmployeeSchema)
async def get_employee_by_id(employee_id: int, db: AsyncSession = Depends(get_db)):
    service = EmployeeService(db)
    try:
        return await service.get_employee_by_id(employee_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Employee not found")
