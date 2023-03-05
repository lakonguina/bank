from sqlalchemy.orm import Session

from fastapi import APIRouter
from fastapi import Depends

from app.dependencies.session import get_db

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate

router = APIRouter()

@router.post("/customer/", response_model=None)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_user = Customer(
        phone=customer.phone,
        email=customer.email,
        first_name=customer.first_name,
        last_name=customer.last_name,
    )

    db.add(db_user)
    db.commit()
