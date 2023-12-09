from datetime import datetime

from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class PhoneField(SQLModel):
    phone: str


class PhoneOut(PhoneField):
    is_valid: bool = Field(default=False)


class Phone(PhoneField, table=True):
	__tablename__ = "phones"

	id_phone: Optional[int] = Field(primary_key=True)
	id_user: int = Field(foreign_key="users.id_user") 
	is_active: bool = Field(default=True)
	date_validation: Optional[datetime]
	date_insert: datetime

	user: "UserFrontoffice" = Relationship(back_populates="phone")
