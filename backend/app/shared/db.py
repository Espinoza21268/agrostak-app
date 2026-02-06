from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.shared.base_model import Base

# Engine de SQLAlchemy
engine = create_engine(
    settings.database_url,
    echo=True,          # pon False en producción
    future=True
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Dependencia para FastAPI
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
