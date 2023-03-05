from fastapi import FastAPI

from app.db.base import Base
from app.db.base import engine

from app.v1 import customer

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customer.router, tags=["customers"])
