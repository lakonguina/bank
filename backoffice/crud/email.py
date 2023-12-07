from pydantic import EmailStr

from sqlmodel import Session, select

from backoffice.schemas.email import Email
from backoffice.schemas.user import User


def get_email(session: Session, email: EmailStr) -> Email:
	return session.exec(
		select(Email)
		.where(Email.email == email)
		.where(Email.is_active == True)
	).first()


def get_email_by_user(session: Session, id_user: int) -> Email:
	return session.exec(
		select(Email)
		.where(Email.id_user == id_user)
	).one()


def get_email_by_id(session: Session, id_email: int) -> Email:
	return session.get(Email, id_email)


def create_email(session: Session, user: User, email: EmailStr) -> Email:
	db_email = Email(
		user=user,
		email=email,
	)
	
	session.add(db_email)
	session.commit()
	session.refresh(db_email)
	
	return db_email
