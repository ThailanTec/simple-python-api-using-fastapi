from core.config import settings

from sqlalchemy import Column, Integer, String


class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(200))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)

