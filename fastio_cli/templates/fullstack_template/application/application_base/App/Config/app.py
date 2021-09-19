import os
import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import (
    BaseSettings, 
    EmailStr, 
    HttpUrl, 
    PostgresDsn, 
    AnyHttpUrl,
    Field,
    validator
)
# Python 3.6+ only
from pathlib import Path  

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

APP_PATH = "{0}".format(Path(CURRENT_DIR).parent)
ENV_PATH = "{0}/.env".format(APP_PATH)
STORAGE_PATH = "{0}/Storage".format(APP_PATH)


class Settings(BaseSettings):
    APP_PATH: str = APP_PATH
    API_ADMIN_PREFIX: str = "/admin"
    API_V1_PREFIX: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

    # App config
    APP_NAME: str = Field('aaa', env='APP_NAME')
    APP_SECRET_KEY: str = secrets.token_urlsafe(32)
    APP_ENV: str = Field(..., env='APP_ENV')
    APP_DEBUG: bool = Field(..., env='APP_DEBUG')
    APP_URL: str = Field(..., env='APP_URL')

    # Database
    DB_CONNECTION: str = Field(..., env='DB_CONNECTION')
    DB_HOST: str = Field('localhost', env='DB_HOST')
    DB_PORT: int = Field(..., env='DB_PORT')
    DB_USER: str = Field(..., env='DB_USER')
    DB_PASSWORD: str = Field(..., env='DB_PASSWORD')
    DB_DATABASE: str = Field('', env='DB_DATABASE')
    DB_PREFIX: str = Field('', env='DB_PREFIX')

    # Logging
    LOG_CHANNEL: str = Field('daily', env='LOG_CHANNEL')
    LOG_LEVEL: str = Field('debug', env='LOG_LEVEL')

    # Cache
    CACHE_DRIVER: str = Field('file', env='CACHE_DRIVER')
    CACHE_MAX_AGE: int = Field(1800, env='CACHE_MAX_AGE')

    # Queue: Redis|Kafka
    QUEUE_DRIVER: str = Field(..., env='QUEUE_DRIVER')

    # Pub/Sub
    PUBSUB_DRIVER: str = Field(..., env='PUBSUB_DRIVER')

    class Config:
        case_sensitive = True
        env_file = ENV_PATH
        env_file_encoding = 'utf-8'


settings = Settings()
