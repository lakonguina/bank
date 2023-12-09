from typing import Optional

from datetime import datetime

from pydantic import EmailStr

from sqlmodel import Field, Relationship, SQLModel


class EmailField(SQLModel):
    email: EmailStr


class EmailOut(EmailField):
	is_valid: bool = Field(default=False)


class Email(EmailOut, table=True):
	__tablename__ = "emails"

	id_email: Optional[int] = Field(primary_key=True)
	id_user: int = Field(foreign_key="users.id_user") 
	is_active: bool = Field(default=True)
	date_validation: Optional[datetime]

	user: Optional["User"] = Relationship(back_populates="email")
