from datetime import datetime

from pydantic import BaseModel, EmailStr

from api.schemas.email import EmailOut
from api.schemas.phone import PhoneOut


class CustomerStatus(BaseModel):
    slug: str
    
    class Config:
        orm_mode = True

class CustomerLogin(BaseModel):
    login: str
    password: str

class CustomerCreate(CustomerLogin):
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
    customer_status: CustomerStatus

    class Config:
        orm_mode = True
