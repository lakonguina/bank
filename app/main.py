from typing import List

import databases
import sqlalchemy
from sqlalchemy.sql import func

from fastapi import FastAPI
from pydantic import BaseModel

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

customers = sqlalchemy.Table(
    "customers",
    metadata,
    sqlalchemy.Column("id_customer", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("phone", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("is_phone_valid", sqlalchemy.Boolean, default=False),
    sqlalchemy.Column("is_email_valid", sqlalchemy.Boolean, default=False),
    sqlalchemy.Column("is_deleted", sqlalchemy.Boolean, default=False),
    sqlalchemy.Column("date_update", sqlalchemy.DateTime, onupdate=func.now()),
    sqlalchemy.Column("date_insert", sqlalchemy.DateTime, server_default=func.now()),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

class Customer(BaseModel):
    phone: str
    email: str 
    first_name: str 
    last_name: str 


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/customer/", response_model=Customer)
async def create_customer(customer: Customer):
    create_customer_query = customers.insert().values(
        phone=customer.phone,
        email=customer.email,
        first_name=customer.first_name,
        last_name=customer.last_name,
    )

    await database.execute(create_customer_qury)

    return {**note.dict()}
