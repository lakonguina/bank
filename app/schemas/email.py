from datetime import datetime
from pydantic import BaseModel, EmailStr

class EmailSend(BaseModel):
    email: EmailStr

class EmailOut(EmailSend):
    is_email_active: bool
    is_active: bool
    date_validation: datetime | None = None
    date_insert: datetime
    
    class Config:
        orm_mode = True
