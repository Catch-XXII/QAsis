from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Artist(Base):
    __tablename__ = "artist"
    artist_id = Column("artist_id", Integer, primary_key=True)
    name = Column("name", String)

    albums = relationship("Album", back_populates="artist")