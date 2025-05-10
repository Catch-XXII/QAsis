# app/api/v1/artists.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db.session import get_db
from backend.app.db.models.artist import Artist
from backend.app.db.schemas.artist_schema import ArtistSchema
from backend.app.services.artist_service import ArtistService
from backend.app.utils.response import format_response_with_headers

router = APIRouter()


@router.get("/artists")
async def get_artists(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(Artist)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(Artist).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Artist)
    response["total"] = total
    return response


@router.get("/artists/search")
async def get_artists_by_name(
    name: str = Query(...),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
):
    total_stmt = (
        select(func.count()).select_from(Artist).where(Artist.name.ilike(f"%{name}%"))
    )
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = (
        select(Artist).where(Artist.name.ilike(f"%{name}%")).offset(skip).limit(limit)
    )
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Artist)
    response["total"] = total
    return response


@router.get("/artists/{artist_id}", response_model=ArtistSchema)
async def get_artist_by_id(artist_id: int, db: AsyncSession = Depends(get_db)):
    service = ArtistService(db)
    try:
        return await service.get_artist_by_id(artist_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Artist not found")
