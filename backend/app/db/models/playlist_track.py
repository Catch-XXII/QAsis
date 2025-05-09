from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base


class PlaylistTrack(Base):
    __tablename__ = "playlist_track"

    playlist_id = Column("playlist_id", Integer, ForeignKey("playlist.playlist_id"), primary_key=True)
    track_id = Column("track_id", Integer, ForeignKey("track.track_id"), primary_key=True)

    track = relationship("Track", lazy="joined")

