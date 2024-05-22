from typing import Optional
from pydantic import BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    id: Optional[int] = None
    title: str
    aulas: int
    horas: int

    class Config:
        from_attributes = True
