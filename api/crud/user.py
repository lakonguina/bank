from pydantic import EmailStr

from sqlalchemy.orm import Session

from api.models.user import UserStatus
from api.models.user import User

from api.schemas.user import UserCreate

from api.dependencies.security import get_password_hash

from api.crud.email import get_email


def get_user_status(db: Session, slug: str) -> UserStatus | None:
	return db.query(UserStatus)\
		.filter(UserStatus.slug == slug)\
		.first()

def get_user_by_email(db: Session, email: EmailStr) -> User:
	email = get_email(db, email)
	
	return db.query(User)\
		.filter(User.id_user == email.id_user)\
		.first()

def get_user_by_id(db: Session, id_user: int) -> User:
	return db.query(User)\
		.filter(User.id_user == id_user)\
		.first()

def create_user(db: Session, user: UserCreate) -> User:
	user_status = get_user_status(db, "waiting-for-validation")

	hashed_password = get_password_hash(user.password)

	db_user = User(
		password=hashed_password,
		first_name=user.first_name,
		last_name=user.last_name,
		id_user_status=user_status.id_user_status,
	)
	
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	
	return db_user
