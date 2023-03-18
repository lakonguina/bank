from sqlalchemy.orm import Session

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
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
from app.models.customer import Customer

from app.schemas.customer import (
    CustomerCreate,
    CustomerOut,
)

from app.schemas.token import Token


router = APIRouter()

@router.post("/customer/register", response_model=CustomerOut)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """Create a customer"""

    # Check if phone not already active and validated
    phone_exists = db.query(Contact)\
        .filter(Contact.phone==customer.contact.phone)\
        .filter(Contact.is_phone_active==True)\
        .first()

    if phone_exists:
        raise HTTPException(
            status_code=400,
            detail="This phone is already registered and active."
        )

    # Check if country exists
    db_country = db.query(Country)\
        .filter(Country.alpha3==customer.country.alpha3)\
        .first()

    if not db_country:
        raise HTTPException(
            status_code=400,
            detail="This country does not exists."
        )

    # Create customer & contact
    hashed_password = get_password_hash(customer.password)

    db_customer = Customer(
        id_country=db_country.id_country,
        first_name=customer.first_name,
        last_name=customer.last_name,
        password=hashed_password,
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    db_contact = Contact(
        id_customer=db_customer.id_customer,
        phone=customer.contact.phone
    )

    db.add(db_contact)
    db.commit()

    db_customer.contact = db_contact

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
