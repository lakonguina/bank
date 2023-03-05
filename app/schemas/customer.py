from pydantic import BaseModel
from pydantic import EmailStr

class CustomerPhone(BaseModel):
    phone: str

class CustomerEmail(BaseModel):
    email: EmailStr

class CustomerCreate(CustomerPhone, CustomerEmail):
    first_name: str
    last_name: str
