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
from api.models.customer import Customer


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
http_bearer =  HTTPBearer()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_token(subject: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {
        "exp": expire, 
        "sub": subject,
    }

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return encoded_jwt


def has_access(
    access_token: HTTPAuthorizationCredentials = Depends(http_bearer),
    db: Session = Depends(get_db),
) -> Customer:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            access_token.credentials,
            key=settings.SECRET_KEY,
            algorithms=settings.JWT_ALGORITHM,
        )

        login: str = payload.get("sub")
        expire: datetime = payload.get("exp")

    except JWTError:
        raise credentials_exception
    
    customer = db.query(Customer)\
            .filter(Customer.login==login)\
            .first()

    return customer

def verify_email(
    token: str,
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            key=settings.SECRET_KEY,
            algorithms=settings.JWT_ALGORITHM,
        )

        email: str = payload.get("sub")
        expire: datetime = payload.get("exp")

    except JWTError as err:
        raise credentials_exception

    return email 
