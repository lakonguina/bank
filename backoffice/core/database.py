from backoffice.core.settings import settings

from sqlmodel import create_engine, Session, SQLModel

database_url_frontoffice = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

database_url_backoffice = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.POSTGRES_PORT}/backoffice"

engine_frontoffice = create_engine(
	database_url_frontoffice,
	echo=True,
)

engine_backoffice = create_engine(
	database_url_backoffice,
	echo=True,
)

SQLModel.metadata.create_all(engine_frontoffice)
SQLModel.metadata.create_all(engine_backoffice)

def get_session_frontoffice():
    with Session(engine_frontoffice) as session:
        yield session

def get_session_backoffice():
    with Session(engine_backoffice) as session:
        yield session
