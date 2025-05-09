from pydantic import BaseModel


class ArtistSchema(BaseModel):
    artist_id: int
    name: str

    class Config:
        from_attributes = True
