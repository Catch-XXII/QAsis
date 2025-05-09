# app/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    API_HOST: str
    API_PORT: int
    FRONTEND_ORIGIN: str


    class Config:
        env_file = ".env"


settings = Settings()
