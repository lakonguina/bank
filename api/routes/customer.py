from datetime import datetime

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

from api.models.customer import Customer
from api.models.phone import Phone
from api.models.email import Email

from api.schemas.customer import (
    CustomerCreate,
    CustomerOut,
    CustomerLogin,
)

from api.schemas.email import EmailSend
from api.schemas.token import Token

from api.crud.customer import create_customer
from api.crud.email import (
	get_email,
	get_email_by_customer,
	create_email,
)
from api.crud.phone import (
	get_phone,
	create_phone,
)

router = APIRouter()


def send_email(to: str):
	try:
		message = MIMEMultipart()
		message['From'] = settings.MAIL_USER
		message['To'] = to
		message['Subject'] = "Test envoi"
		body = MIMEText("Message de test", 'plain')

		message.attach(body)

		with SMTP(settings.MAIL_HOST, settings.MAIL_PORT) as server:
			server.starttls()
			server.login(settings.MAIL_USER, settings.MAIL_PASSWORD)
			server.send_message(message)

	except Exception as e:
		print(e)

@router.post("/customer/register", response_model=None)
def register_customer(
    customer: CustomerCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
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

	# Create customer & contact
	db_customer = create_customer(db, customer)

	create_email(db, customer.id_customer, customer.email)
	create_phone(db, customer.id_customer, customer.phone)

	#background_tasks.add_task(send_email, customer.email)

	return {"detail": "Customer created"}

@router.post("/customer/login", response_model=Token)
def login_customer(customer: CustomerLogin, db: Session = Depends(get_db)):
    db_customer = db.query(Customer)\
        .filter(Customer.login==customer.login)\
        .first()

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

@router.post("/customer/email/send", response_model=None)
def send_email_customer(
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
    
    token = create_token(email.email)

    url = f"http://localhost:8080/customer/email/verify/{token}"

    print('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{')
    print('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{')
    print(url)
    print('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{')
    print('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{')

    #background_tasks.add_task(send_email, email.email)
    
    return {"detail": "Email sended."}

@router.get("/customer/email/verify/{token}", response_model=None)
def customer_verify_email(
    token: str,
    db: Session = Depends(get_db),
):
    sub = verify_email(token)

    email = get_email(db, sub)

    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email not found."
        )

    if email.is_email_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already validated."
        )

    email.is_email_active = True
    email.date_validation = datetime.now()

    db.add(email)
    db.commit()
    db.refresh(email)
    
    print(email.__dict__)

    return {"detail": "Email validated"}
