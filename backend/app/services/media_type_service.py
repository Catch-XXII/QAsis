from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.media_type import MediaType


class MediaTypeService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_media_types(self):
        result = await self.db.execute(select(MediaType))
        return result.scalars().all()

    async def get_media_type_by_id(self, media_type_id: int):
        result = await self.db.execute(select(MediaType).where(MediaType.media_type_id == media_type_id))
        media_type = result.scalar_one_or_none()
        if media_type is None:
            raise NoResultFound(f"MediaType ID {media_type_id} not found")
        return media_type

    async def search_media_types(self, name=None):
        stmt = select(MediaType)
        if name:
            stmt = stmt.where(MediaType.name.ilike(f"%{name}%"))
        result = await self.db.execute(stmt)
        return result.scalars().all()