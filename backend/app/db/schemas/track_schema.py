from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class TrackSchema(BaseModel):
    track_id: int
    name: str
    album_id: Optional[int] = None
    media_type_id: int
    genre_id: Optional[int] = None
    composer: Optional[str] = None
    milliseconds: int
    bytes: Optional[int] = None
    unit_price: Decimal

    class Config:
        from_attributes = True
