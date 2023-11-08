from datetime import datetime

from pydantic import BaseModel, EmailStr

from app.schemas.country import (
    CountryAlpha3,
    CountryOut,
)

from app.schemas.email import (
    EmailCreate,
    EmailOut,
)

from app.schemas.phone import (
    PhoneCreate,
    PhoneOut,
)


class CustomerCreate(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str


class CustomerOut(BaseModel):
    login: str
    first_name: str
    last_name: str
    date_insert: datetime
    email: EmailOut
    phone: PhoneOut

    class Config:
        orm_mode = True
