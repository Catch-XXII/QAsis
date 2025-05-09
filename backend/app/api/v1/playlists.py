from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import SessionLocal
from app.db.models.playlist import Playlist
from app.db.schemas.playlist_schema import PlaylistSchema
from app.services.playlist_service import PlaylistService
from app.utils.response import format_response_with_headers

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session


@router.get("/playlists")
async def get_playlists(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(Playlist)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(Playlist).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Playlist)
    response["total"] = total
    return response


@router.get("/playlists/search")
async def search_playlists(
    name: str = Query(...),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Playlist).where(Playlist.name.ilike(f"%{name}%"))

    total_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()

    response = format_response_with_headers(rows, Playlist)
    response["total"] = total
    return response


@router.get("/playlists/{playlist_id}", response_model=PlaylistSchema)
async def get_playlist_by_id(playlist_id: int, db: AsyncSession = Depends(get_db)):
    service = PlaylistService(db)
    try:
        return await service.get_playlist_by_id(playlist_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Playlist not found")
