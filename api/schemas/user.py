from datetime import datetime

from pydantic import (
	BaseModel,
	EmailStr,
	Field
)

from api.schemas.email import EmailOut
from api.schemas.phone import PhoneOut


class UserStatus(BaseModel):
    slug: str
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    login: str = Field(title="Login of the user", max_length=64)
    password: str = Field(title="Password of the user", max_length=64)

class UserCreate(UserLogin):
    first_name: str = Field(title="Only the first first name of the user", max_length=64)
    last_name: str = Field(title="Last name of the user", max_length=64)
    email: EmailStr = Field(title="Email of the user")
    phone: str = Field(title="Phone number of the user", max_length=16)

class UserOut(BaseModel):
    login: str
    first_name: str
    last_name: str
    date_insert: datetime
    email: EmailOut
    phone: PhoneOut
    user_status: UserStatus

    class Config:
        orm_mode = True
