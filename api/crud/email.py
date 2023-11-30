from sqlalchemy.orm import Session

from api.models.email import Email


def get_email(db: Session, email: str) -> Email | None:
	return db.query(Email).filter(Email.email == email, Email.is_active == True).first()

def get_email_by_customer(db: Session, id_customer: int) -> Email | None:
	return db.query(Email).filter(Email.id_customer == id_customer, Email.is_active == True).first()

def create_email(db: Session, id_customer: int, email: str) -> Email:
	db_email = Email(
		id_customer=id_customer,
		email=email,
	)
	
	db.add(db_email)
	db.commit()
	db.refresh(db_email)
	
	return db_email
