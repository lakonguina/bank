from sqlalchemy.orm import Session

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from app.dependencies.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    has_access,
)

from app.dependencies.session import get_db

from app.models.contact import Contact
from app.models.country import Country
from app.models.customer import Customer, CustomerStatus
from app.models.phone import Phone
from app.models.email import Email

from app.schemas.customer import (
    CustomerCreate,
    CustomerOut,
)

from app.schemas.token import Token


router = APIRouter()

@router.post("/customer/register", response_model=CustomerOut)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """Create a customer"""

    phone = db.query(Phone)\
        .filter(Phone.phone==customer.phone)\
        .filter(Phone.is_phone_active==True)\
        .filter(Phone.is_active==True)\
        .first()

    if phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone is already registered and active."
        )

    email = db.query(Email)\
        .filter(Email.email==customer.phone)\
        .filter(Email.is_email_active==True)\
        .filter(Email.is_active==True)\
        .first()

    if email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered and active."
        )

    # Create customer & contact
    hashed_password = get_password_hash(customer.password)

    customer_status = db.query(CustomerStatus)\
        .filter(CustomerStatus.slug=="waiting-for-email")\
        .first()

    print('_______________________________________________')
    print(customer_status)
    print('_______________________________________________')

    db_customer = Customer(
        login=customer.login,
        password=hashed_password,
        first_name=customer.first_name,
        last_name=customer.last_name,
        id_customer_status=customer_status.id_customer_status,
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    db_phone = Phone(
        id_customer=db_customer.id_customer,
        phone=customer.phone
    )

    db_email= Email(
        id_customer=db_customer.id_customer,
        email=customer.email
    )

    db.add(db_phone)
    db.commit()
    db.refresh(db_phone)

    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    db_customer.phone = db_phone
    db_customer.email= db_email

    return db_customer

"""
@router.post("/customer/login", response_model=Token)
async def login_customer(customer: CustomerLogin, db: Session = Depends(get_db)):
    db_customer = db.query(Customer)\
        .filter(Customer.phone==customer.phone)\
        .first()

    if not db_customer:
        raise HTTPException(
            status_code=200,
            detail="Wrong credentials."
        )
    
    password_is_good = verify_password(customer.password, db_customer.password)

    if not password_is_good:
        raise HTTPException(
            status_code=200,
            detail="Wrong credentials."
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
    pass
"""
