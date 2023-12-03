from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.base import Base
from api.core.base import engine

from api.routes import customer

api = FastAPI(
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

origins = [
    "http://localhost",
    "http://0.0.0.0:3000",
    "http://0.0.0.0:7000",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(customer.router, tags=["Customers"])

Base.metadata.create_all(bind=engine)
