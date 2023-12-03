from datetime import datetime

from sqlalchemy.orm import Session

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    HTTPException,
    status,
)

from api.core.settings import settings

from api.dependencies.security import (
    verify_password,
    create_token,
    has_access,
    verify_email,
)

from api.dependencies.session import get_db
from api.dependencies.email import validate_email 

from api.schemas.customer import (
    CustomerCreate,
    CustomerLogin,
    CustomerOut,
)

from api.schemas.token import Token

from api.crud.customer import (
	create_customer,
	get_customer_by_login,
)

from api.crud.email import (
	get_email,
	get_email_by_customer,
	create_email,
)

from api.crud.phone import (
	get_phone,
	get_phone_by_customer,
	create_phone,
)


router = APIRouter()

@router.post("/customer/register", response_model=None)
def customer_register(
    customer: CustomerCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
	# Check if phone and email are not used
	phone = get_phone(db, customer.phone)

	if phone:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Phone is already registered and active."
		)

	email = get_phone(db, customer.email)

	if email:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email is already registered and active."
		)

	# Create customer
	db_customer = create_customer(db, customer)

	# Create phone and email
	create_email(db, db_customer.id_customer, customer.email)
	create_phone(db, db_customer.id_customer, customer.phone)

	# Send email to validate email
	token = create_token(customer.email)
	url = f"{settings.URI}/customer/email/verify/{token}"

	background_tasks.add_task(
		validate_email,
		customer.email,
		url,
	)

	# TODO: Send message to validate phone

	return {"detail": "Customer created check your email for validation"}


@router.post("/customer/login", response_model=Token)
def login_customer(customer: CustomerLogin, db: Session = Depends(get_db)):
    db_customer = get_customer_by_login(db, customer.login)

    if not db_customer:
        raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Wrong login."
		)
    
    password_is_good = verify_password(customer.password, db_customer.password)

    if not password_is_good:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Wrong password."
        )
     
    access_token = create_token(db_customer.login)
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/customer/login", response_model=Token)
def customer_login(customer: CustomerLogin, db: Session = Depends(get_db)):
    db_customer = get_customer_by_login(db, customer.login)

    if not db_customer:
        raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Wrong login."
		)
    
    password_is_good = verify_password(customer.password, db_customer.password)

    if not password_is_good:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Wrong password."
        )
     
    access_token = create_token(db_customer.login)
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/customer/email/send", response_model=None)
def customer_send_email(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    customer = Depends(has_access),
):
	email = get_email_by_customer(db, customer.id_customer)

	if email.is_email_active == True:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email is already validated."
		)

	# Send email to validate email
	token = create_token(email.email)
	url = f"{settings.URI}/customer/email/verify/{token}"
	
	background_tasks.add_task(
		validate_email,
		email.email,
		url,
	)

	return {"detail": "Email sended"}


@router.get("/customer/email/verify/{token}", response_model=None)
def customer_verify_email(
    token: str,
    db: Session = Depends(get_db),
):
	email = verify_email(token)
	db_email = get_email(db, email)

	if not db_email:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email not found."
		)

	if db_email.is_email_active:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email already validated."
		)

	db_email.is_email_active = True
	db_email.date_validation = datetime.now()

	db.add(db_email)
	db.commit()
	db.refresh(db_email)

	return {"detail": "Email validated"}

@router.get("/customer/information", response_model=CustomerOut)
def customer_information(
    db: Session = Depends(get_db),
    customer = Depends(has_access),
):
	customer.email = get_email_by_customer(db, customer.id_customer)
	customer.phone = get_phone_by_customer(db, customer.id_customer)
	
	return customer
