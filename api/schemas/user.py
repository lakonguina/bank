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


class UserEmail(BaseModel):
    email: EmailStr = Field(title="Email of the user")


class UserPassword(BaseModel):
    password: str = Field(title="Password of the user", max_length=64)


class UserLoginByEmail(UserEmail, UserPassword):
	pass


class UserCreate(UserLoginByEmail):
    first_name: str = Field(title="Only the first first name of the user", max_length=64)
    last_name: str = Field(title="Last name of the user", max_length=64)
    phone: str = Field(title="Phone number of the user", max_length=16)


class UserOut(BaseModel):
    first_name: str
    last_name: str
    date_insert: datetime
    email: EmailOut
    phone: PhoneOut
    user_status: UserStatus

    class Config:
        orm_mode = True
