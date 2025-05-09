from sqlalchemy import Column, Integer, String

from app.db.database import Base


class MediaType(Base):
    __tablename__ = "media_type"

    media_type_id = Column("media_type_id", Integer, primary_key=True)
    name = Column("name", String, nullable=True)
