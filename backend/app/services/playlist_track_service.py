from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.models.playlist_track import PlaylistTrack


class PlaylistTrackService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_playlist_tracks(self):
        result = await self.db.execute(select(PlaylistTrack))
        return result.scalars().all()

    async def get_playlist_tracks_with_track_data(self, skip: int = 0, limit: int = 10):
        stmt = (
            select(PlaylistTrack)
            .options(selectinload(PlaylistTrack.track))
            .offset(skip)
            .limit(limit)
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()