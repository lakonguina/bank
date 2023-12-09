from typing import Optional

from datetime import datetime

from pydantic import EmailStr

from sqlmodel import Field, Relationship, SQLModel


class Address(SQLModel, table=True):
	__tablename__ = "addresses"

	id_address: int = Field(primary_key=True)
	id_user: int = Field(foreign_key="users.id_user") 
	alpha3: str = Field(foreign_key="countries.alpha3") 

	street: str
	city: str
	zip_code: str
	is_active: bool
	date_insert: datetime

	user: Optional["UserFrontoffice"] = Relationship(back_populates="address")
	country: Optional["Country"] = Relationship(back_populates="address")
