from typing import Optional

from pydantic import BaseModel


class PlaylistSchema(BaseModel):
    playlist_id: int
    name: Optional[str] = None

    class Config:
        from_attributes = True
