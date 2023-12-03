from datetime import datetime
from pydantic import BaseModel, EmailStr

class EmailSend(BaseModel):
    email: EmailStr

class EmailOut(EmailSend):
    is_email_active: bool
    
    class Config:
        orm_mode = True
