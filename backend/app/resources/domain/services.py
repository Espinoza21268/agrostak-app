from sqlalchemy.orm import Session
from typing import List, Optional
from app.resources.infra.repository import RecursoRepository
from app.resources.domain.schemas import (
    RecursoCreate,
    RecursoUpdate,
    RecursoRead,
)


def listar_recursos(db: Session) -> List[RecursoRead]:
    repo = RecursoRepository(db)
    recursos = repo.listar()
    return [RecursoRead.from_orm(r) for r in recursos]


def obtener_recurso(db: Session, id_recurso: int) -> Optional[RecursoRead]:
    repo = RecursoRepository(db)
    recurso = repo.obtener(id_recurso)
    if not recurso:
        return None
    return RecursoRead.from_orm(recurso)


def crear_recurso(db: Session, data: RecursoCreate) -> RecursoRead:
    repo = RecursoRepository(db)
    recurso = repo.crear(data)
    return RecursoRead.from_orm(recurso)


def actualizar_recurso(db: Session, id_recurso: int, data: RecursoUpdate) -> Optional[RecursoRead]:
    repo = RecursoRepository(db)
    recurso = repo.actualizar(id_recurso, data)
    if not recurso:
        return None
    return RecursoRead.from_orm(recurso)


def eliminar_recurso(db: Session, id_recurso: int) -> bool:
    repo = RecursoRepository(db)
    return repo.eliminar(id_recurso)
