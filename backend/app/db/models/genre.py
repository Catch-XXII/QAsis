from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Genre(Base):
    __tablename__ = "genre"  #

    genre_id = Column("genre_id", Integer, primary_key=True)
    name = Column("name", String)

    tracks = relationship("Track", back_populates="genre")