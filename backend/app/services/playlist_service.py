from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.playlist import Playlist


class PlaylistService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_playlists(self):
        result = await self.db.execute(select(Playlist))
        return result.scalars().all()

    async def get_playlist_by_id(self, playlist_id: int):
        result = await self.db.execute(select(Playlist).where(Playlist.playlist_id == playlist_id))
        playlist = result.scalar_one_or_none()
        if playlist is None:
            raise NoResultFound(f"Playlist ID {playlist_id} not found")
        return playlist

    async def search_playlists(self, name=None):
        stmt = select(Playlist)
        if name:
            stmt = stmt.where(Playlist.name.ilike(f"%{name}%"))
        result = await self.db.execute(stmt)
        return result.scalars().all()