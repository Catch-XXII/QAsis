from typing import Optional

from pydantic import BaseModel


class TrackSchema(BaseModel):
    track_id: int
    name: str
    composer: Optional[str] = None
    milliseconds: int

    class Config:
        from_attributes = True


class PlaylistTrackWithTrackSchema(BaseModel):
    playlist_id: int
    track: TrackSchema

    class Config:
        from_attributes = True
