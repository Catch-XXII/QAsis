from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Genre


class GenreService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_genres(self):
        result = await self.db.execute(select(Genre))
        return result.scalars().all()

    async def get_genre_by_id(self, genre_id: int):
        result = await self.db.execute(select(Genre).where(Genre.genre_id == genre_id))
        genre = result.scalar_one_or_none()
        if genre is None:
            raise NoResultFound(f"Genre ID {genre_id} not found")
        return genre

    async def search_genres(self, name=None):
        stmt = select(Genre)
        if name:
            stmt = stmt.where(Genre.name.ilike(f"%{name}%"))
        result = await self.db.execute(stmt)
        return result.scalars().all()