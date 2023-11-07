from datetime import datetime
from pydantic import BaseModel, EmailStr

class EmailCreate(BaseModel):
    email: EmailStr

class EmailOut(EmailCreate):
    is_email_active: bool
    is_active: bool
    date_validation: datetime | None = None
    date_insert: datetime | None = None
    
    class Config:
        orm_mode = True
