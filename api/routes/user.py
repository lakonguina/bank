from datetime import datetime

from pydantic import EmailStr

from fastapi import APIRouter, Depends, HTTPException

from sqlmodel import Session

from api.core.database import engine, get_session
from api.core.settings import settings

from api.dependencies.security import password_check, verify_password, create_jwt, decode_jwt, has_access, get_password_hash, JWTSlug

from api.dependencies.email import validate_email, reset_password

from api.schemas.detail import Detail
from api.schemas.user import User, UserCreate, UserInformation, UserLoginByEmail, UserPasswordField, UserStatus
from api.schemas.token import Token
from api.schemas.email import Email, EmailField

from api.crud.email import get_email, get_email_by_id, get_email_by_user
from api.crud.phone import get_phone, get_phone_by_user
from api.crud.user import create_user, get_user_by_email, get_user_by_id


router = APIRouter(tags=["Users"])

@router.post("/user/register", response_model=Detail)
def user_register(
	user: UserCreate,
	session: Session = Depends(get_session),
):
	#print(user.password)
	#test = password_check(user.password)
	#print(test)
	# Check if phone and email are not used
	email = get_email(session, user.email)

	if email:
		raise HTTPException(
			status_code=409,
			detail="Email is already registered and active"
		)

	phone = get_phone(session, user.phone)

	if phone:
		raise HTTPException(
			status_code=409,
			detail="Phone is already registered and active"
		)

	password_res: dict[str, bool] = password_check(user.password)
	
	if not password_res['password_ok']:
		raise HTTPException(
			status_code=409,
			detail=password_res,
		)

	# Create user
	db_email = create_user(session, user)

	# Send email to validate email
	token = create_jwt(
		str(db_email.id_email),
		JWTSlug.verify_email,
	)

	url = f"{settings.URI_FRONTEND}/validate-email/{token}"

	validate_email(user.email, url)

	# TODO: Send message to validate phone

	return {"detail": "User created check your email for validation"}


@router.post("/user/login/email", response_model=Token)
def user_login_by_email(
	user: UserLoginByEmail,
	session: Session = Depends(get_session),
):
	db_user = get_user_by_email(session, user.email)

	if not db_user:
		raise HTTPException(
			status_code=400,
			detail="Wrong email"
		)

	password_is_good = verify_password(user.password, db_user.password)

	if not password_is_good:
		raise HTTPException(
			status_code=400,
			detail="Wrong password"
		)

	access_token = create_jwt(
		str(db_user.id_user),
		JWTSlug.access,
	)

	return {
		"access_token": access_token,
		"token_type": "bearer"
	}


@router.get("/user/email/send/verification-email/", response_model=Detail)
def user_send_email(
	session: Session = Depends(get_session),
    id_user: int = Depends(has_access),
):
	db_email = get_email_by_user(session, id_user)

	if db_email.is_valid == True:
		raise HTTPException(
			status_code=400,
			detail="Email is already validated"
		)

	jwt = create_jwt(
		str(db_email.id_email),
		JWTSlug.verify_email,
	)

	url = f"{settings.URI_FRONTEND}/validate-email/{jwt}"

	validate_email(db_email.email, url)

	return {"detail": "Email sended"}


@router.get("/user/email/verify/{jwt}", response_model=None)
def user_verify_email(
    jwt: str,
	session: Session = Depends(get_session),
):
	id_email: int = decode_jwt(jwt, JWTSlug.verify_email)
	db_email = get_email_by_id(session, id_email)

	if not db_email:
		raise HTTPException(
			status_code=400,
			detail="Email not found"
		)

	if db_email.is_valid:
		raise HTTPException(
			status_code=400,
			detail="Email already validated"
		)

	db_email.is_valid = True
	db_email.date_validation = datetime.now()

	session.add(db_email)
	session.commit()

	return {"detail": "Email validated"}


@router.get("/user/information", response_model=UserInformation)
def user_information(
	session: Session = Depends(get_session),
    id_user: int = Depends(has_access),
):
	db_user = get_user_by_id(session, id_user)

	return db_user

@router.post("/user/email/send/reset-password", response_model=Detail)
def user_reset_password_by_email(
	email: EmailField,
	session: Session = Depends(get_session),
):
	db_user = get_user_by_email(session, email.email)

	if not db_user:
		raise HTTPException(
			status_code=400,
			detail="Email not found"
		)

	token: str = create_jwt(
		str(db_user.id_user),
		JWTSlug.reset_password,
	)

	url = f"{settings.URI_FRONTEND}/validate-email/{token}"

	reset_password(email.email, url)
	
	return {"detail": "Your password reset link as been sent at your email"}


@router.post("/user/reset-password/{jwt}", response_model=Detail)
def user_reset_password(
    jwt: str,
	password: UserPasswordField,
	session: Session = Depends(get_session),
):
	id_user: int  = decode_jwt(jwt, JWTSlug.reset_password)

	db_user = get_user_by_id(session, id_user)

	hashed_password = get_password_hash(password.password)
	db_user.password = hashed_password

	session.add(db_user)
	session.commit()

	return {"detail": "Password updated"}
