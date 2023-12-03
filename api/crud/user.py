from sqlalchemy.orm import Session

from api.models.user import UserStatus
from api.models.user import User

from api.schemas.user import UserCreate

from api.dependencies.security import get_password_hash


def get_user_status(db: Session, slug: str) -> UserStatus | None:
	return db.query(UserStatus)\
		.filter(UserStatus.slug == slug)\
		.first()

def get_user_by_login(db: Session, login: str) -> User:
	return db.query(User)\
		.filter(User.login == login)\
		.first()

def create_user(db: Session, user: UserCreate) -> User:
	user_status = get_user_status(db, "waiting-for-email")

	hashed_password = get_password_hash(user.password)

	db_user = User(
		login=user.login,
		password=hashed_password,
		first_name=user.first_name,
		last_name=user.last_name,
		id_user_status=user_status.id_user_status,
	)
	
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	
	return db_user
