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
    first_name: str
    last_name: str
    password: str
    phone: str
    email: EmailStr

class CustomerOut(BaseModel):
    first_name: str
    last_name: str
    is_active: bool
    date_insert: datetime
    country: CountryOut

    class Config:
        orm_mode = True
