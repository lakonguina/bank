import os

from pydantic import BaseSettings

class Settings(BaseSettings):
	PROJECT_NAME: str = "Bank" 
	URL: str = os.environ.get("API_URL")
	PORT: str = os.environ.get("API_PORT")
	URI: str = f"{URL}:{PORT}"

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
	# MAIL_TLS: str = os.environ.get("MAIL_TLS") TODO: Handle this with env
	MAIL_HOST: str = os.environ.get("MAIL_HOST")
	MAIL_PORT: int  = os.environ.get("MAIL_PORT")
	MAIL_USER: str = os.environ.get("MAIL_USER")
	MAIL_NAME: str = "Bank"
	MAIL_PASSWORD: str = os.environ.get("MAIL_PASSWORD")

	# TEMPLATES
	TEMPLATES_DIR: str = '/app/api/templates'

	class Config:
		case_sensitive = True

settings = Settings()
