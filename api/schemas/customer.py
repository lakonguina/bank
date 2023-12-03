from datetime import datetime

from pydantic import (
	BaseModel,
	EmailStr,
	Field
)

from api.schemas.email import EmailOut
from api.schemas.phone import PhoneOut


class CustomerStatus(BaseModel):
    slug: str
    
    class Config:
        orm_mode = True

class CustomerLogin(BaseModel):
    login: str = Field(title="Login of the customer", max_length=64)
    password: str = Field(title="Password of the customer", max_length=64)

class CustomerCreate(CustomerLogin):
    first_name: str = Field(title="Only the first first name of the customer", max_length=64)
    last_name: str = Field(title="Last name of the customer", max_length=64)
    email: EmailStr = Field(title="Email of the customer")
    phone: str = Field(title="Phone number of the customer", max_length=16)

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
