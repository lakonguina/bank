from sqlalchemy.orm import Session

from api.models.phone import Phone


def get_phone(db: Session, phone: str) -> Phone | None:
	return db.query(Phone).filter(Phone.phone == phone, Phone.is_active==True).first()

def create_phone(db: Session, id_customer: int, phone: str) -> Phone:
	db_phone = Phone(
		id_customer=id_customer,
		phone=phone,
	)
	
	db.add(db_phone)
	db.commit()
	db.refresh(db_phone)
	
	return db_phone
