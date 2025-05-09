# app/db/schemas.py
from pydantic import BaseModel


class AlbumSchema(BaseModel):
    album_id: int
    artist_id: int
    title: str

    class Config:
        from_attributes = True
