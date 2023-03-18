from datetime import datetime

from pydantic import BaseModel

from app.schemas.country import (
    CountryAlpha3,
    CountryOut,
)

from app.schemas.contact import (
    ContactPhone,
    ContactOut,
)


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    password: str
    country: CountryAlpha3
    contact: ContactPhone

class CustomerOut(BaseModel):
    first_name: str
    last_name: str
    is_active: bool
    date_insert: datetime
    country: CountryOut
    contact: ContactOut

    class Config:
        orm_mode = True
