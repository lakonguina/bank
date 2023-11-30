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
    get_password_hash,
    verify_password,
    create_token,
    has_access,
    verify_email,
)

from api.dependencies.session import get_db

from api.models.customer import (
    Customer,
    CustomerStatus,
)

from api.models.phone import Phone
from api.models.email import Email

from api.schemas.customer import (
    CustomerCreate,
    CustomerOut,
    CustomerLogin,
)

from api.schemas.email import EmailSend
from api.schemas.token import Token

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
		raise HTTPException(status_code=500, detail=f"Erreur lors de l'envoi de l'email.")

@router.post("/customer/register", response_model=CustomerOut)
def create_customer(
    customer: CustomerCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    phone = db.query(Phone)\
        .filter(Phone.phone==customer.phone)\
        .first()

    if phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone is already registered and active."
        )

    email = db.query(Email)\
        .filter(Email.email==customer.phone)\
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
    db_customer.email = db_email
    db_customer.customer_status = customer_status

    background_tasks.add_task(send_email, customer.email)

    return db_customer

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
    access = Depends(has_access),
):
    email = db.query(Email)\
        .filter(Email.id_customer==access.id_customer)\
        .filter(Email.is_active==True)\
        .first()

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

    email = db.query(Email)\
        .filter(Email.email==sub)\
        .first()

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

"""
@router.post("/customer/send/phone", response_model=None)
def send_customer_phone(
        customer: CustomerPhone,
        db: Session = Depends(get_db),
        access = Depends(has_access),
    ):
    pass
"""
