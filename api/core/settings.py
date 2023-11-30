import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Security
    SECRET_KEY: str = os.environ.get("API_SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 60
    JWT_ALGORITHM: str = "HS256"

    # Database
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOSTNAME: str = os.environ.get("POSTGRES_HOSTNAME")
    POSTGRES_PORT: int = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")

    # SMTP
    MAIL_HOST: str = os.environ.get("MAIL_HOST")
    MAIL_PORT: int  = os.environ.get("MAIL_PORT")
    MAIL_USER: str = os.environ.get("MAIL_USER")
    MAIL_PASSWORD: str = os.environ.get("MAIL_PASSWORD")

    class Config:
        case_sensitive = True

settings = Settings()
