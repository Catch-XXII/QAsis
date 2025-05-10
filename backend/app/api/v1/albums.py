from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db
from backend.app.db.models.album import Album
from backend.app.db.schemas.album_schema import AlbumSchema
from backend.app.services.album_service import AlbumService
from backend.app.utils.response import format_response_with_headers

router = APIRouter()


@router.get("/albums")
async def get_albums(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(Album)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(Album).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Album)
    response["total"] = total
    return response


@router.get("/albums/search")
async def get_albums_by_title(
    title: str, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    total_stmt = (
        select(func.count()).select_from(Album).where(Album.title.ilike(f"%{title}%"))
    )
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = (
        select(Album).where(Album.title.ilike(f"%{title}%")).offset(skip).limit(limit)
    )
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Album)
    response["total"] = total
    return response


@router.get("/albums/{album_id}", response_model=AlbumSchema)
async def get_album_by_id(album_id: int, db: AsyncSession = Depends(get_db)):
    service = AlbumService(db)
    try:
        return await service.get_album_by_id(album_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Album not found")
