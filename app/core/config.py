import os
from typing import List

from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl


env = os.getenv("ENV") or "development"
env_dir = os.getenv("ENV_DIR") or os.getcwd()


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_V1_STR: str = "/api/v1"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # DB_NAME: str
    # DB_HOST: str
    # DB_PORT: str
    # DB_USER: str
    # DB_PASSW: str

    DB_STR_CONNECTION: str

    class Config:
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings(_env_file=f"{env_dir}/environments/.env.{env}", ENVIRONMENT=env)
