from typing import Optional

from pydantic import EmailStr

from fastapi import HTTPException

from sqlmodel import Session, select

from api.schemas.user import User, UserCreate, UserStatus
from api.schemas.email import Email
from api.schemas.phone import Phone
from api.schemas.address import Address

from api.crud.email import get_email
from api.crud.country import get_country

from api.dependencies.security import get_password_hash


def get_user_status(session: Session, slug: str) -> UserStatus | None:
	return session.exec(select(UserStatus).where(UserStatus.slug == slug)).one()

def get_user_by_id(session: Session, id_user: int) -> User:
	return session.get(User, id_user)

def get_user_by_email(session: Session, email: EmailStr) -> User:
	db_email = get_email(session, email)
	db_user: Optional[User] = None

	if db_email:
		db_user = get_user_by_id(session, db_email.id_user)	

	return db_user

def create_user(session: Session, user: UserCreate) -> User:
	nationality = get_country(session, user.country.alpha3)
	
	if not nationality:
		raise HTTPException(
			status_code=400,
			detail="The country of your nationality do not exist",
		)
		
	residence = get_country(session, user.address.alpha3)

	if not residence:
		raise HTTPException(
			status_code=400,
			detail="The country of your nationality do not exist",
		)

	status = get_user_status(session, "waiting-for-validation")
	hashed_password = get_password_hash(user.password)

	db_user = User(
		password=hashed_password,
		first_name=user.first_name,
		last_name=user.last_name,
		status=status,
		alpha3=user.country.alpha3,
	)
	
	db_address = Address(
		user=db_user,
		street=user.address.street,	
		alpha3=user.address.alpha3,	
		city=user.address.city,
		zip_code=user.address.zip_code,	
	)
	
	db_email = Email(
		user=db_user,
		email=user.email,
	)

	db_phone = Phone(
		user=db_user,
		phone=user.phone,
	)
	
	session.add(db_user)
	session.add(db_address)
	session.add(db_email)
	session.add(db_phone)

	session.commit()
	
	session.refresh(db_email)
	
	return db_email
