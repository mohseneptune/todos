from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_DIRECTORY: Path = Path(__file__).resolve().parent.parent.parent
    APP_NAME: str
    DEBUG: bool

    # Database configuration
    DATABASE_DRIVERNAME: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    model_config = SettingsConfigDict(
        env_file=BASE_DIRECTORY / ".env",
        env_file_encoding="utf-8",
    )


settings = Settings()  # type: ignore
