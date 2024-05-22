from http import HTTPStatus
from typing import List
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schemas.curso_schemas import CursoSchema

from core.deps import get_session

router = APIRouter()


@router.post('/', status_code=HTTPStatus.CREATED, response_model=CursoSchema)
async def create_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    new_curso = CursoModel(title=curso.title, aulas=curso.aulas, horas=curso.horas)
    db.add(new_curso)
    await db.commit()
    return new_curso


@router.get('/', response_model=List[CursoSchema])
async def get_all_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()

        return cursos


@router.get('/{id}', response_model=CursoSchema, status_code=HTTPStatus.OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        if curso:
            return curso
        else:
            raise HTTPException(detail="Curso não encontrado", status_code=HTTPStatus.NOT_FOUND)


@router.put('/{id}', response_model=CursoSchema, status_code=HTTPStatus.OK)
async def update_curso(curso_id: int, data: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up = result.scalar_one_or_none()
        if curso_up:
            curso_up.title = data.title
            curso_up.aulas = data.aulas
            curso_up.horas = data.horas
            await session.commit()
            return curso_up
        else:
            raise HTTPException(detail="Curso não encontrado para atualizar", status_code=HTTPStatus.NOT_FOUND)


@router.delete('/{id}', status_code=HTTPStatus.OK)
async def update_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_deleted = result.scalar_one_or_none()
        if curso_deleted:
            await session.delete(curso_deleted)
            await session.commit()
            return HTTPStatus.NO_CONTENT
        else:
            raise HTTPException(detail="Curso não encontrado para deletar", status_code=HTTPStatus.NOT_FOUND)
