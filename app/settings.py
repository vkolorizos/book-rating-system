from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    title: str = "BookRatingSystem API"
    version: str = "v.0.1"
    origins: List[str] = ['*']


config = Settings()
