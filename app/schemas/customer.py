from pydantic import BaseModel

class CustomerCreate(BaseModel):
    phone: str
    email: str
    first_name: str
    last_name: str
