from datetime import datetime

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import SecretStr

class CustomerPhone(BaseModel):
    phone: str

class CustomerEmail(BaseModel):
    email: EmailStr

class CustomerLogin(CustomerPhone):
    password: str

class CustomerCreate(CustomerLogin, CustomerEmail):
    first_name: str
    last_name: str

class CustomerOut(
        CustomerPhone,
        CustomerEmail
    ):
    first_name: str
    last_name: str

    is_active: bool
    is_email_active: bool
    is_phone_active: bool
    
    date_email: datetime
    date_phone: datetime
    date_insert: datetime

    class Config:
        orm_mode = True
