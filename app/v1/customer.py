from sqlalchemy.orm import Session

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.dependencies.session import get_db

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate
from app.schemas.customer import CustomerPhone

router = APIRouter()

@router.post("/customer/register", response_model=None)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    customer_exists = db.query(Customer)\
        .filter((Customer.phone==customer.phone) | (Customer.email==customer.email))\
        .filter(Customer.is_active==True)\
        .first()

    if customer_exists:
        if customer_exists.phone == customer.phone:
            raise HTTPException(
                status_code=200,
                detail="This phone is already registered and active."
            )

        if customer_exists.email == customer.email:
            raise HTTPException(
                status_code=200,
                detail="This email is already registered and active."
            )

    db_customer = Customer(
        phone=customer.phone,
        email=customer.email,
        first_name=customer.first_name,
        last_name=customer.last_name,
    )

    db.add(db_customer)
    db.commit()

@router.post("/customer/send/phone", response_model=None)
async def send_customer_phone(customer: CustomerPhone, db: Session = Depends(get_db)):
    customer_exists = db.query(Customer)\
        .filter(Customer.phone==customer.phone, Customer.is_active==False)\
        .first()

    print('_______________________________________')
    print('_______________________________________')
    print(customer.date_email)
    print(customer.date_phone)
    print('_______________________________________')
    print('_______________________________________')

@router.post("/customer/send/email", response_model=None)
async def send_customer_email(customer: CustomerPhone, db: Session = Depends(get_db)):
    customer_exists = db.query(Customer)\
        .filter(Customer.email==customer.email, Customer.is_active==False)\
        .first()
