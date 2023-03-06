from datetime import (
    datetime,
    timedelta,
)

from typing import (
    Any,
    Union,
)

from pydantic import ValidationError

from jose import (
    jwt,
    JWTError,
)

from passlib.context import CryptContext

from fastapi import Depends

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from app.core.settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
http_bearer =  HTTPBearer()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(subject: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {
        "exp": expire, 
        "sub": subject,
    }

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return encoded_jwt


def has_access(access_token: HTTPAuthorizationCredentials = Depends(http_bearer)):
    """
        Function that is used to validate the token in the case that it requires it
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )

    try:
        payload = jwt.decode(
            access_token.credentials,
            key=settings.SECRET_KEY,
            algorithms=settings.JWT_ALGORITHM,
        )

        username: str = payload.get("sub")

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail='Authorization token expired'
        )

    except jwt.JWTClaimsError:
        raise HTTPException(
            status_code=401,
            detail='Incorrect claims, check the audience and issuer.'
        )

    except Exception:
        raise HTTPException(
            status_code=401,
            detail='Unable to parse authentication token'
        )

    print(payload)

    return payload
