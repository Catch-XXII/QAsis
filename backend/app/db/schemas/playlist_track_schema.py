from pydantic import BaseModel


class PlaylistTrackSchema(BaseModel):
    playlist_id: int
    track_id: int

    class Config:
        from_attributes = True
