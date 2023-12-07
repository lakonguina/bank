from sqlmodel import Session, select

from backoffice.schemas.phone import Phone
from backoffice.schemas.user import User


def get_phone(session: Session, phone: str) -> Phone:
	return session.exec(
		select(Phone)
		.where(Phone.phone == phone)
		.where(Phone.is_active == True)
	).first()


def get_phone_by_user(session: Session, id_user: int) -> Phone:
	return session.exec(
		select(Phone)
		.where(Phone.id_user == id_user)
	).one()


def create_phone(session: Session, user: User, phone: str) -> Phone:
	db_phone = Email(
		user=user,
		phone=phone,
	)
	
	session.add(db_phone)
	session.commit()
	session.refresh(db_phone)
	
	return db_phone
