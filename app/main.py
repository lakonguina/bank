from fastapi import FastAPI

from app.core.base import Base
from app.core.base import engine

from app.api import customer

app = FastAPI(
    title="Bank",
    description="Bank helps you do awesome stuff.",
    version="0.0.1",
    terms_of_service="http://example.com/",
    contact={
        "name": "Bank",
        "url": "http://example.com/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(customer.router, tags=["Customers"])

Base.metadata.create_all(bind=engine)
