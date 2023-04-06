import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    generalPosrgres: str = Field(..., env='GENERAL_DATABASE_URL')

settings = Settings()