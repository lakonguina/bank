from datetime import datetime
from pydantic import BaseModel

class PhoneCreate(BaseModel):
    phone: str

class PhoneOut(PhoneCreate):
    is_phone_active: bool
    is_active: bool
    date_validation: datetime | None = None
    date_insert: datetime | None = None
    
    class Config:
        orm_mode = True
