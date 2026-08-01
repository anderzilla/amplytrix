from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="AMPLYTRIX_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: Literal["local", "development", "staging", "production"] = "local"
    log_level: str = "INFO"
    port: int = Field(default=8080, ge=1, le=65535)
    request_timeout_seconds: float = Field(default=30.0, gt=0, le=300)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
