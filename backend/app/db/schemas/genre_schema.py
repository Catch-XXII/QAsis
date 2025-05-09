from pydantic import BaseModel


class GenreSchema(BaseModel):
    genre_id: int
    name: str

    class Config:
        from_attributes = True
