from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Album


class AlbumService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_albums(self):
        result = await self.db.execute(select(Album))
        return result.scalars().all()

    async def get_album_by_id(self, album_id: int):
        result = await self.db.execute(select(Album).where(Album.album_id == album_id))
        album = result.scalar_one_or_none()
        if album is None:
            raise NoResultFound(f"Album ID {album_id} not found")
        return album

    async def get_albums_by_title(self, title: str):
        stmt = select(Album).where(Album.title.ilike(f"%{title}%"))
        result = await self.db.execute(stmt)
        return result.scalars().all()