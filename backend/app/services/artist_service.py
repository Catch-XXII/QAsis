# app/services/artist_service.py
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Artist


class ArtistService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_artists(self):
        result = await self.db.execute(select(Artist))
        return result.scalars().all()

    async def get_artist_by_id(self, artist_id: int):
        result = await self.db.execute(select(Artist).where(Artist.artist_id == artist_id))
        artist = result.scalar_one_or_none()
        if artist is None:
            raise NoResultFound(f"Artist ID {artist_id} not found")
        return artist

    async def get_artists_by_name(self, name: str):
        result = await self.db.execute(select(Artist).where(Artist.name.ilike(f"%{name}%")))
        return result.scalars().all()