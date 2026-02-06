from sqlalchemy import Column, Integer, String, Enum, Numeric
from app.shared.base_model import Base
from app.resources.domain.entities import TipoRecurso, EstadoRecurso


class RecursoORM(Base):
    __tablename__ = "recursos"

    id_recurso = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(255))
    tipo = Column(Enum(TipoRecurso), nullable=False)
    unidad_medida = Column(String(20), nullable=False)
    cantidad_disponible = Column(Numeric(10, 2), nullable=False, default=0)
    ubicacion = Column(String(100))
    estado = Column(Enum(EstadoRecurso), nullable=False, default=EstadoRecurso.operativo)
