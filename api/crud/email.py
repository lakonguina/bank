from sqlalchemy.orm import Session

from api.models.email import Email


def get_email(db: Session, email: str) -> Email | None:
	return db.query(Email).filter(Email.email == email, Email.is_active == True).first()

def get_email_by_id(db: Session, id_email: int) -> Email | None:
	return db.query(Email).filter(Email.id_email== id_email, Email.is_active == True).first()

def get_email_by_user(db: Session, id_user: int) -> Email | None:
	return db.query(Email).filter(Email.id_user == id_user, Email.is_active == True).first()

def create_email(db: Session, id_user: int, email: str) -> Email:
	db_email = Email(
		id_user=id_user,
		email=email,
	)
	
	db.add(db_email)
	db.commit()
	db.refresh(db_email)
	
	return db_email
