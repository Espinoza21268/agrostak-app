from sqlalchemy.orm import Session

from app.notifications.infra.models import NotificacionORM
from app.notifications.domain.schemas import NotificacionCreate


class NotificationsRepository:
    def __init__(self, db: Session):
        self.db = db

    def crear(self, data: NotificacionCreate) -> NotificacionORM:
        notificacion = NotificacionORM(
            id_usuario=data.id_usuario,
            id_tarea=data.id_tarea,
            id_recurso=data.id_recurso,
            tipo=data.tipo,
            mensaje=data.mensaje,
            leida=0
        )
        self.db.add(notificacion)
        self.db.commit()
        self.db.refresh(notificacion)
        return notificacion

    def listar_por_usuario(self, id_usuario: int):
        return (
            self.db.query(NotificacionORM)
            .filter(NotificacionORM.id_usuario == id_usuario)
            .order_by(NotificacionORM.fecha_envio.desc())
            .all()
        )

    def marcar_leida(self, id_notificacion: int):
        notificacion = (
            self.db.query(NotificacionORM)
            .filter(NotificacionORM.id_notificacion == id_notificacion)
            .first()
        )
        if notificacion:
            notificacion.leida = 1
            self.db.commit()
            self.db.refresh(notificacion)
        return notificacion