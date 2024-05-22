from sqlalchemy.ext.declarative import declarative_base
from pydantic_settings import BaseSettings
from fastapi.templating import Jinja2Templates
from pathlib import Path
from sqlalchemy.ext.declarative import DeclarativeMeta

from typing import ClassVar


class Settings(BaseSettings):
    """
    Configurações Gerais utilizada na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:python@localhost:5432/postgres'
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    TEMPLATE: ClassVar[Jinja2Templates] = Jinja2Templates(directory="templates")
    MEDIA: ClassVar[Path] = Path("media")

    class Config:
        case_sensitive = True


settings: Settings = Settings()
