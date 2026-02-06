from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.shared.db import get_session
from app.identity.infra.repository import IdentityRepository
from app.identity.infra.security import decode_token
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/identity/login")


def get_current_user(db: Session = Depends(get_session), token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token, getattr(settings, "JWT_SECRET", "dev_secret_change_me"))
        user_id = int(payload.get("sub"))
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido.")

    repo = IdentityRepository(db)
    user = repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado.")
    if user.estado != "activo":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuario inactivo.")
    return user
