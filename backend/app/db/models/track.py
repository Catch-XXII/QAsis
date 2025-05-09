from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Track(Base):
    __tablename__ = "track"

    track_id = Column("track_id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    album_id = Column("album_id", Integer, ForeignKey("album.album_id"), nullable=True)
    media_type_id = Column(
        "media_type_id", Integer, ForeignKey("media_type.media_type_id"), nullable=False
    )
    genre_id = Column("genre_id", Integer, ForeignKey("genre.genre_id"), nullable=True)
    composer = Column("composer", String, nullable=True)
    milliseconds = Column("milliseconds", Integer, nullable=False)
    bytes = Column("bytes", Integer, nullable=True)
    unit_price = Column("unit_price", Numeric, nullable=False)

    album = relationship("Album", back_populates="tracks")
    genre = relationship("Genre", back_populates="tracks")