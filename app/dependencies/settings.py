from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "secret_key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 60

    class Config:
        case_sensitive = True

settings = Settings()
