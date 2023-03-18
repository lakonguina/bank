from datetime import datetime
from pydantic import BaseModel


class ContactPhone(BaseModel):
    phone: str


class ContactOut(ContactPhone):
    is_phone_active: bool
    is_active: bool
    date_phone: datetime | None = None
    
    class Config:
        orm_mode = True
