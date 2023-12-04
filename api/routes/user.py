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
    get_token,
    has_access,
	get_password_hash,
)

from api.dependencies.session import get_db
from api.dependencies.email import (
	validate_email,
	reset_password,
)

from api.schemas.user import (
    UserCreate,
    UserLogin,
    UserOut,
	UserReset,
	UserResetPassword,
)

from api.schemas.token import Token
from api.schemas.detail import Detail

from api.crud.user import (
	create_user,
	get_user_by_login,
)

from api.crud.email import (
	get_email,
	get_email_by_user,
	create_email,
)

from api.crud.phone import (
	get_phone,
	get_phone_by_user,
	create_phone,
)


router = APIRouter()

@router.post("/user/register", response_model=Detail)
def user_register(
    user: UserCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
	# Check if phone and email are not used
	email = get_email(db, user.email)

	if email:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Email is already registered and active."
		)

	phone = get_phone(db, user.phone)

	if phone:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Phone is already registered and active."
		)

	# Create user
	db_user = create_user(db, user)

	# Create phone and email
	create_email(db, db_user.id_user, user.email)
	create_phone(db, db_user.id_user, user.phone)

	# Send email to validate email
	token = create_token(user.email)
	url = f"{settings.URI}/user/email/verify/{token}"

	background_tasks.add_task(
		validate_email,
		user.email,
		url,
	)

	# TODO: Send message to validate phone

	return {"detail": "User created check your email for validation"}


@router.post("/user/login", response_model=Token)
def user_login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_login(db, user.login)

    if not db_user:
        raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Wrong login."
		)
    
    password_is_good = verify_password(user.password, db_user.password)

    if not password_is_good:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Wrong password."
        )
     
    access_token = create_token(db_user.login)
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/user/email/send/verification-email/", response_model=Detail)
def user_send_email(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    user = Depends(has_access),
):
	email = get_email_by_user(db, user.id_user)

	if email.is_email_active == True:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email is already validated."
		)

	# Send email to validate email
	token = create_token(email.email)
	url = f"{settings.URI}/user/email/verify/{token}"
	
	background_tasks.add_task(
		validate_email,
		email.email,
		url,
	)

	return {"detail": "Email sended"}


@router.get("/user/email/verify/{token}", response_model=None)
def user_verify_email(
    token: str,
    db: Session = Depends(get_db),
):
	email = get_token(token)
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

	return {"detail": "Email validated"}

@router.get("/user/information", response_model=UserOut)
def user_information(
    db: Session = Depends(get_db),
    user = Depends(has_access),
):
	user.email = get_email_by_user(db, user.id_user)
	user.phone = get_phone_by_user(db, user.id_user)
	
	return user


@router.post("/user/email/send/reset-password", response_model=Detail)
def user_reset_password_by_email(
	login: UserReset,	
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
	user = get_user_by_login(db, login.login)
	email = get_email_by_user(db, user.id_user)

	if not user:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Login not found."
		)

	token = create_token(login.login)
	url = f"{settings.URI}/user/reset-password/{token}"

	background_tasks.add_task(
		reset_password,
		email.email,
		url,
	)
	
	return {"detail": "Your password reset link as been sent at your email"}


@router.post("/user/phone/send/reset-password", response_model=Detail)
def user_reset_password_by_phone(
	login: UserReset,	
):
	# TODO: Handle reset by password


	return {"msg": "Your password reset link as been sent at your phone"}


@router.post("/user/reset-password/{token}", response_model=Detail)
def user_reset_password(
    token: str,
	password: UserResetPassword,
    db: Session = Depends(get_db),
):
	# JWT pass as a string
	login = get_token(token)

	user = get_user_by_login(db, login)

	hashed_password = get_password_hash(password.password)
	user.password = hashed_password

	db.add(user)
	db.commit()

	return {"detail": "Password updated"}
