from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.db.session import get_db
from backend.app.db.models.playlist_track import PlaylistTrack
from backend.app.services.playlist_track_service import PlaylistTrackService
from backend.app.utils.response import format_response_with_headers

router = APIRouter()


@router.get("/playlist-tracks")
async def get_playlist_tracks(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    total_stmt = select(func.count()).select_from(PlaylistTrack)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    data_stmt = select(PlaylistTrack).offset(skip).limit(limit)
    data_result = await db.execute(data_stmt)
    rows = data_result.scalars().all()

    response = format_response_with_headers(rows, PlaylistTrack)
    response["total"] = total
    return response


@router.get("/playlist-tracks/full")
async def get_playlist_tracks_full(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    service = PlaylistTrackService(db)

    full_data = await service.get_playlist_tracks_with_track_data(
        skip=skip, limit=limit
    )

    total_stmt = select(func.count()).select_from(PlaylistTrack)
    total_result = await db.execute(total_stmt)
    total = total_result.scalar()

    headers = [
        {"title": "Playlist ID", "key": "playlist_id", "align": "end"},
        {"title": "Track ID", "key": "track_id", "align": "end"},
        {"title": "Track Name", "key": "track_name", "align": "start"},
        {"title": "Album Title", "key": "album_title", "align": "start"},
        {"title": "Artist", "key": "artist_name", "align": "start"},
    ]

    response = {
        "headers": headers,
        "rows": full_data,
        "total": total,
    }

    return response
