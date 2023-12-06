from datetime import (
    datetime,
    timedelta,
)

from typing import (
    Any,
    Union,
)

from sqlalchemy.orm import Session

from jose import (
    jwt,
    JWTError,
)

from passlib.context import CryptContext

from fastapi import (
    Depends,
    HTTPException,
    status,
)

from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)

from api.dependencies.session import get_db
from api.core.settings import settings
from api.models.user import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
http_bearer =  HTTPBearer()

credentials_exception = HTTPException(
	status_code=status.HTTP_401_UNAUTHORIZED,
	detail="Could not validate credentials",
	headers={"WWW-Authenticate": "Bearer"},
)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_jwt(sub: str, use: str) -> str:
    exp = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "exp": exp, # Expiration
        "sub": sub, # Subject eg: id_user, id_email
        "use": use, # Use of this JWT eg: login, reset-password-be-email
    }

    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return encoded_jwt


def has_access(
    access_token: HTTPAuthorizationCredentials = Depends(http_bearer),
    db: Session = Depends(get_db),
) -> User:
	try:
		payload = jwt.decode(
			access_token.credentials,
			key=settings.SECRET_KEY,
			algorithms=settings.JWT_ALGORITHM,
		)

		sub: str = payload.get("sub")
		use: str = payload.get("use")

		if use != "access":
			raise HTTPException(
				status_code=400,
				detail="Wrong token use"
			)

	except JWTError as error:
		raise credentials_exception

	user = db.query(User)\
		.filter(User.id_user==int(sub))\
		.first()

	return user

def decode_jwt(jwt_in: str):
	try:
		payload = jwt.decode(
			jwt_in,
			key=settings.SECRET_KEY,
			algorithms=settings.JWT_ALGORITHM,
		)

		sub: str = payload.get("sub")
		use: str = payload.get("use")

	except JWTError as err:
		raise credentials_exception

	return int(sub), use
