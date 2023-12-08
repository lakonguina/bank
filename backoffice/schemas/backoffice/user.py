from pydantic import EmailStr
from typing import Optional
from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class UserLogin(SQLModel):
	email: str = Field(max_length=320)
	password: str = Field(max_length=64)


class UserBackoffice(UserLogin, table=True):
	__tablename__ = "users_internal"

	id_user_internal: Optional[int] = Field(primary_key=True)
	first_name: str = Field(max_length=64)
	last_name: str = Field(max_length=64)
	password: str = Field(max_length=64)
	date_insert: datetime
