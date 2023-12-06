from datetime import datetime, timedelta

from jose import jwt, JWTError

from passlib.context import CryptContext

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from api.core.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
http_bearer =  HTTPBearer()

credentials_exception = HTTPException(
	status_code=status.HTTP_401_UNAUTHORIZED,
	detail="Could not validate credentials",
	headers={"WWW-Authenticate": "Bearer"},
)

class JWTSlug:
	access = "access"
	verify_email = "verify_email"
	reset_password = "reset_password"

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


def decode_jwt(jwt_in: str, use_in: str) -> int:
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
	
	if use_in != use:
		raise HTTPException(
			status_code=409,
			detail=f"Wrong jwt use should be {use_in} instead of {use}"
		)

	return int(sub)


def has_access(jwt_in: HTTPAuthorizationCredentials = Depends(http_bearer)) -> int:
	sub: int = decode_jwt(jwt_in.credentials, JWTSlug.access)

	return sub
