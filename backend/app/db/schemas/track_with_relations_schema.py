from pydantic import BaseModel


class ArtistNested(BaseModel):
    artist_id: int
    name: str

    class Config:
        from_attributes = True

class AlbumNested(BaseModel):
    album_id: int
    title: str
    artist: ArtistNested

    class Config:
        from_attributes = True

class GenreNested(BaseModel):
    genre_id: int
    name: str

    class Config:
        from_attributes = True

class TrackWithRelations(BaseModel):
    track_id: int
    name: str
    composer: str | None
    milliseconds: int
    unit_price: float
    album: AlbumNested
    genre: GenreNested

    class Config:
        from_attributes = True
