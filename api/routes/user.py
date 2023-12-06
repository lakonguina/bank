from datetime import datetime

from sqlalchemy.orm import Session

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from api.core.settings import settings

from api.dependencies.security import (
    verify_password,
    create_jwt,
    decode_jwt,
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
    UserLoginByEmail,
    UserOut,
	UserEmail,
	UserPassword,
)

from api.schemas.token import Token
from api.schemas.detail import Detail

from api.crud.user import (
	create_user,
	get_user_by_email,
	get_user_by_id,
)

from api.crud.email import (
	get_email,
	get_email_by_id,
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
    db: Session = Depends(get_db)
):
	# Check if phone and email are not used
	email = get_email(db, user.email)

	if email:
		raise HTTPException(
			status_code=409,
			detail="Email is already registered and active"
		)

	phone = get_phone(db, user.phone)

	if phone:
		raise HTTPException(
			status_code=409,
			detail="Phone is already registered and active"
		)

	# Create user
	db_user = create_user(db, user)

	# Create phone and email
	db_email = create_email(db, db_user.id_user, user.email)
	db_phone = create_phone(db, db_user.id_user, user.phone)

	# Send email to validate email
	token = create_jwt(str(db_email.id_email), "verify-email")
	url = f"{settings.URI}/user/email/verify/{token}"

	validate_email(user.email, url)

	# TODO: Send message to validate phone

	return {"detail": "User created check your email for validation"}


@router.post("/user/login/email", response_model=Token)
def user_login_by_email(user: UserLoginByEmail, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)

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
     
    access_token = create_jwt(str(db_user.id_user), "access")
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/user/email/send/verification-email/", response_model=Detail)
def user_send_email(
    db: Session = Depends(get_db),
    user = Depends(has_access),
):
	db_email = get_email_by_user(db, user.id_user)

	if db_email.is_email_active == True:
		raise HTTPException(
			status_code=400,
			detail="Email is already validated"
		)

	jwt = create_jwt(str(db_email.id_email), "verify-email")
	url = f"{settings.URI}/user/email/verify/{jwt}"

	validate_email(db_email.email, url)

	return {"detail": "Email sended"}


@router.get("/user/email/verify/{jwt}", response_model=None)
def user_verify_email(
    jwt: str,
    db: Session = Depends(get_db),
):
	id_email, use = decode_jwt(jwt)

	if use != "verify-email":
		raise HTTPException(
			status_code=400,
			detail="Wrong jwt use"
		)
		
	db_email = get_email_by_id(db, id_email)

	if not db_email:
		raise HTTPException(
			status_code=400,
			detail="Email not found"
		)

	if db_email.is_email_active:
		raise HTTPException(
			status_code=400,
			detail="Email already validated"
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
	email: UserEmail,
    db: Session = Depends(get_db),
):
	db_user = get_user_by_email(db, email.email)

	if not db_user:
		raise HTTPException(
			status_code=400,
			detail="Email not found"
		)

	token = create_jwt(str(db_user.id_user), "reset-password")
	url = f"{settings.URI}/user/email/verify/{token}"

	validate_email(email.email, url)
	
	return {"detail": "Your password reset link as been sent at your email"}


@router.post("/user/reset-password/{token}", response_model=Detail)
def user_reset_password(
    token: str,
	password: UserPassword,
    db: Session = Depends(get_db),
):
	id_user, use = decode_jwt(token)

	if use != "reset-password":
		raise HTTPException(
			status_code=400,
			detail="Wrong jwt use"
		)

	user = get_user_by_id(db, id_user)

	hashed_password = get_password_hash(password.password)
	user.password = hashed_password

	db.add(user)
	db.commit()

	return {"detail": "Password updated"}
