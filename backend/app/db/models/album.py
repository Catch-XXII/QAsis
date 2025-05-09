from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.db.models.base_mixin import TableHeaderMixin


class Album(Base, TableHeaderMixin):
    __tablename__ = "album"

    album_id = Column("album_id", Integer, primary_key=True)
    artist_id = Column("artist_id", Integer, ForeignKey("artist.artist_id"))
    title = Column("title", String)

    artist = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="album")