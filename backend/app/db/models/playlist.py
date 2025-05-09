from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Playlist(Base):
    __tablename__ = "playlist"

    playlist_id = Column("playlist_id", Integer, primary_key=True)
    name = Column("name", String, nullable=True)
