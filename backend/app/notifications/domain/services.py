from sqlalchemy.orm import Session

from app.notifications.infra.repository import NotificationsRepository
from app.notifications.domain.schemas import NotificacionCreate, NotificacionRead


def guardar_notificacion(db: Session, data: NotificacionCreate) -> NotificacionRead:
    print("entra a guardar notificacion")
    repo = NotificationsRepository(db)
    row = repo.crear(data)
    return NotificacionRead.model_validate(row)


def listar_notificaciones_usuario(db: Session, id_usuario: int) -> list[NotificacionRead]:
    repo = NotificationsRepository(db)
    rows = repo.listar_por_usuario(id_usuario)
    return [NotificacionRead.model_validate(x) for x in rows]


def marcar_notificacion_leida(db: Session, id_notificacion: int):
    repo = NotificationsRepository(db)
    row = repo.marcar_leida(id_notificacion)
    if row:
        return NotificacionRead.model_validate(row)
    return None