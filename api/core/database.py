from api.core.settings import settings

from sqlmodel import create_engine, Session, SQLModel

database_url = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(
	database_url,
	echo=True,
)

SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
