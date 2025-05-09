from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import SessionLocal
from app.db.models.track import Track
from app.db.schemas.track_schema import TrackSchema
from app.db.schemas.track_with_relations_schema import TrackWithRelations
from app.services.track_service import TrackService
from app.utils.response import format_response_with_headers

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.get("/tracks")
async def get_tracks(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(Track)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(Track).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, Track)
    response["total"] = total
    return response


@router.get("/tracks/search")
async def search_tracks(
    name: str | None = Query(None),
    composer: str | None = Query(None),
    genre_id: int | None = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Track)

    if name:
        stmt = stmt.where(Track.name.ilike(f"%{name}%"))
    if composer:
        stmt = stmt.where(Track.composer.ilike(f"%{composer}%"))
    if genre_id:
        stmt = stmt.where(Track.genre_id == genre_id)

    total_stmt = select(func.count()).select_from(stmt.subquery())
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()

    response = format_response_with_headers(rows, Track)
    response["total"] = total
    return response


@router.get("/tracks/{track_id}", response_model=TrackSchema)
async def get_track_by_id(track_id: int, db: AsyncSession = Depends(get_db)):
    service = TrackService(db)
    try:
        return await service.get_track_by_id(track_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Track not found")


@router.get("/tracks/{track_id}/full", response_model=TrackWithRelations)
async def get_track_with_details(track_id: int, db: AsyncSession = Depends(get_db)):
    service = TrackService(db)
    return await service.get_track_with_relations(track_id)
