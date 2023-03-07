from pydantic import BaseSettings

class Settings(BaseSettings):
    # SECURITY
    SECRET_KEY: str = "secret_key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 60
    JWT_ALGORITHM: str = "HS256"


    # DATABASE
    POSTGRES_USER = "test"
    POSTGRES_PASSWORD = "test"
    POSTGRES_HOSTNAME = "db"
    POSTGRES_PORT = "5432"
    POSTGRES_DB = "test"

    class Config:
        case_sensitive = True

settings = Settings()
