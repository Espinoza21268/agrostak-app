from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func

from app.shared.base_model import Base


class NotificacionORM(Base):
    __tablename__ = "notificaciones"

    id_notificacion = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_tarea = Column(Integer, ForeignKey("tareas.id_tarea"), nullable=True)
    id_recurso = Column(Integer, ForeignKey("recursos.id_recurso"), nullable=True)

    tipo = Column(
        Enum(
            "tarea_asignada",
            "proxima_vencer",
            "vencida",
            "bajo_stock",
            "mantenimiento",
            name="tipo_notificacion_enum"
        ),
        nullable=False
    )

    mensaje = Column(String(255), nullable=False)
    fecha_envio = Column(DateTime, nullable=False, server_default=func.now())
    leida = Column(Integer, nullable=False, default=0)