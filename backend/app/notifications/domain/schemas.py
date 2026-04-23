from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class NotificacionCreate(BaseModel):
    id_usuario: int
    id_tarea: Optional[int] = None
    id_recurso: Optional[int] = None
    tipo: Literal[
        "tarea_asignada",
        "proxima_vencer",
        "vencida",
        "bajo_stock",
        "mantenimiento"
    ]
    mensaje: str


class NotificacionRead(BaseModel):
    id_notificacion: int
    id_usuario: int
    id_tarea: Optional[int] = None
    id_recurso: Optional[int] = None
    tipo: str
    mensaje: str
    fecha_envio: datetime
    leida: int

    class Config:
        from_attributes = True