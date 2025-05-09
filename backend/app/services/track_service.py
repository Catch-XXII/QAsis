from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.models.album import Album
from app.db.models.track import Track


class TrackService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_tracks(self):
        result = await self.db.execute(select(Track))
        return result.scalars().all()

    async def get_track_by_id(self, track_id: int):
        result = await self.db.execute(select(Track).where(Track.track_id == track_id))
        track = result.scalar_one_or_none()
        if track is None:
            raise NoResultFound(f"Track ID {track_id} not found")
        return track

    async def search_tracks(self, name=None, composer=None, genre_id=None):
        stmt = select(Track)
        if name:
            stmt = stmt.where(Track.name.ilike(f"%{name}%"))
        if composer:
            stmt = stmt.where(Track.composer.ilike(f"%{composer}%"))
        if genre_id:
            stmt = stmt.where(Track.genre_id == genre_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_track_with_relations(self, track_id: int):
        stmt = (
            select(Track)
            .where(Track.track_id == track_id)
            .options(
                selectinload(Track.album).selectinload(Album.artist),
                selectinload(Track.genre)
            )
        )
        result = await self.db.execute(stmt)
        track = result.scalar_one_or_none()
        if not track:
            raise NoResultFound("Track not found")
        return track