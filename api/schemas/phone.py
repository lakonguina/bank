from datetime import datetime
from pydantic import BaseModel

class PhoneCreate(BaseModel):
    phone: str

class PhoneOut(PhoneCreate):
    is_phone_active: bool
    
    class Config:
        orm_mode = True
