from sqlalchemy.orm import Session

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.dependencies.session import get_db
from app.dependencies.security import get_password_hash
from app.dependencies.security import verify_password
from app.dependencies.security import create_access_token
from app.dependencies.security import has_access

from app.models.customer import Customer

from app.schemas.customer import CustomerCreate
from app.schemas.customer import CustomerLogin
from app.schemas.customer import CustomerPhone
from app.schemas.customer import CustomerEmail
from app.schemas.customer import CustomerOut

from app.schemas.token import Token


router = APIRouter()

@router.post("/customer/register", response_model=CustomerOut)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    customer_exists = db.query(Customer)\
        .filter((Customer.phone==customer.phone) | (Customer.email==customer.email))\
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

    hashed_password = get_password_hash(customer.password)

    db_customer = Customer(
        phone=customer.phone,
        email=customer.email,
        first_name=customer.first_name,
        last_name=customer.last_name,
        password=hashed_password,
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


@router.post("/customer/login", response_model=Token)
async def login_customer(customer: CustomerLogin, db: Session = Depends(get_db)):
    db_customer = db.query(Customer)\
        .filter(Customer.phone==customer.phone)\
        .first()

    if not db_customer:
        raise HTTPException(
            status_code=200,
            detail="This phone is not registered."
        )
    
    password_is_good = verify_password(customer.password, db_customer.password)

    if not password_is_good:
        raise HTTPException(
            status_code=200,
            detail="This password or phone is wrong."
        )
     
    access_token = create_access_token(db_customer.phone)
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/customer/send/phone", response_model=None)
async def send_customer_phone(
        customer: CustomerPhone,
        db: Session = Depends(get_db),
        access = Depends(has_access),
    ):
    customer_exists = db.query(Customer)\
        .filter(Customer.phone==customer.phone, Customer.is_active==False)\
        .first()

    if customer_exists:
        pass

@router.post("/customer/send/email", response_model=None)
async def send_customer_email(customer: CustomerEmail, db: Session = Depends(get_db)):
    customer_exists = db.query(Customer)\
        .filter(Customer.email==customer.email, Customer.is_active==False)\
        .first()
