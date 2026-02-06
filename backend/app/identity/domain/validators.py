import re

def validate_password_strength(password: str) -> None:
    # mínimo 8, 1 mayúscula, 1 minúscula, 1 número
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    if not re.search(r"[A-Z]", password):
        raise ValueError("La contraseña debe tener al menos 1 letra mayúscula.")
    if not re.search(r"[a-z]", password):
        raise ValueError("La contraseña debe tener al menos 1 letra minúscula.")
    if not re.search(r"\d", password):
        raise ValueError("La contraseña debe tener al menos 1 número.")
