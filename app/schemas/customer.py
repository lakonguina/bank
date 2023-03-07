from datetime import datetime

from pydantic import BaseModel


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str


class CustomerOut(BaseModel):
    first_name: str
    last_name: str

    is_active: bool
    is_email_active: bool
    is_phone_active: bool
    
    date_email: datetime
    date_phone: datetime
    date_update: datetime
    date_insert: datetime

    class Config:
        orm_mode = True
