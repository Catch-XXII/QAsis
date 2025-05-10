from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.db.session import get_db
from backend.app.db.models.media_type import MediaType
from backend.app.db.schemas.media_type_schema import MediaTypeSchema
from backend.app.services.media_type_service import MediaTypeService
from backend.app.utils.response import format_response_with_headers

router = APIRouter()


@router.get("/media-types")
async def get_media_types(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(MediaType)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(MediaType).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, MediaType)
    response["total"] = total
    return response


@router.get("/media-types/search")
async def search_media_types(
    name: str = Query(...),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(MediaType).where(MediaType.name.ilike(f"%{name}%"))

    total_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()

    response = format_response_with_headers(rows, MediaType)
    response["total"] = total
    return response


@router.get("/media-types/{media_type_id}", response_model=MediaTypeSchema)
async def get_media_type_by_id(media_type_id: int, db: AsyncSession = Depends(get_db)):
    service = MediaTypeService(db)
    try:
        return await service.get_media_type_by_id(media_type_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Media type not found")
