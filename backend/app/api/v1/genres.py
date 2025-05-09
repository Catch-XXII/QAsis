from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import SessionLocal
from app.db.models.genre import Genre
from app.db.schemas.genre_schema import GenreSchema
from app.services.genre_service import GenreService
from app.utils.response import format_response_with_headers

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.get("/genres")
async def get_genres(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(Genre)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(Genre).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Genre)
    response["total"] = total
    return response


@router.get("/genres/search")
async def search_genres(
    name: str = Query(...),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Genre).where(Genre.name.ilike(f"%{name}%"))

    # total count with subquery
    total_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    # paginated
    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()

    response = format_response_with_headers(rows, Genre)
    response["total"] = total
    return response


@router.get("/genres/{genre_id}", response_model=GenreSchema)
async def get_genre_by_id(genre_id: int, db: AsyncSession = Depends(get_db)):
    service = GenreService(db)
    try:
        return await service.get_genre_by_id(genre_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Genre not found")
