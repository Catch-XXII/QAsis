from typing import Optional

from pydantic import BaseModel


class MediaTypeSchema(BaseModel):
    media_type_id: int
    name: Optional[str] = None

    class Config:
        from_attributes = True
