from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = "root"
    DB_PASSWORD: str = "Kripton12"
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "flor_canela_db"

    JWT_SECRET: str = "cambia_esto_por_algo_largo"
    JWT_EXPIRES_MIN: int = 120

    @property
    def database_url(self) -> str:
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"  # si luego quieres sobrescribir con variables de entorno


settings = Settings()