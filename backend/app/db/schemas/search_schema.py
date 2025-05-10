# app/db/schemas/search_schema.py

from pydantic import BaseModel, HttpUrl


class SearchRequestSchema(BaseModel):
    query: HttpUrl
