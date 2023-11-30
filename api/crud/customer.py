from sqlalchemy.orm import Session

from api.models.customer import CustomerStatus
from api.models.customer import Customer

from api.schemas.customer import CustomerCreate

from api.dependencies.security import get_password_hash


def get_customer_status(db: Session, slug: str) -> CustomerStatus | None:
	return db.query(CustomerStatus)\
		.filter(CustomerStatus.slug == slug)\
		.first()

def get_customer_by_login(db: Session, login: str) -> Customer:
	return db.query(Customer)\
		.filter(Customer.login == login)\
		.first()

def create_customer(db: Session, customer: CustomerCreate) -> Customer:
	customer_status = get_customer_status(db, "waiting-for-email")

	hashed_password = get_password_hash(customer.password)

	db_customer = Customer(
		login=customer.login,
		password=hashed_password,
		first_name=customer.first_name,
		last_name=customer.last_name,
		id_customer_status=customer_status.id_customer_status,
	)
	
	db.add(db_customer)
	db.commit()
	db.refresh(db_customer)
	
	return db_customer
