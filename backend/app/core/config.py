# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    API_HOST: str
    API_PORT: int
    FRONTEND_ORIGIN: str

    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # New structure for getting settings v2.x
    model_config = SettingsConfigDict(env_file=".env")

    # Old structure according to pydantic v1.x
    # class Config:
    #     env_file = ".env"


settings = Settings()
