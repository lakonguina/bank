from sqlalchemy.orm import Session

from api.models.phone import Phone


def get_phone(db: Session, phone: str) -> Phone | None:
	return db.query(Phone).filter(Phone.phone == phone, Phone.is_active==True).first()

def get_phone_by_user(db: Session, id_user: int) -> Phone | None:
	return db.query(Phone).filter(Phone.id_user == id_user, Phone.is_active==True).first()

def create_phone(db: Session, id_user: int, phone: str) -> Phone:
	db_phone = Phone(
		id_user=id_user,
		phone=phone,
	)
	
	db.add(db_phone)
	db.commit()
	db.refresh(db_phone)
	
	return db_phone
