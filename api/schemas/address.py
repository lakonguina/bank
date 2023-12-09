from typing import Optional

from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from api.schemas.country import Country


class AddressBase(SQLModel):
	street: str = Field(max_length=64)
	city: str = Field(max_length=64)
	zip_code: str = Field(max_length=64)


class AddressIn(AddressBase):
	alpha3: str = Field(foreign_key="countries.alpha3")


class AddressOut(AddressBase):
	country: Country
	

class Address(AddressIn, table=True):
	__tablename__ = "addresses"

	id_address: Optional[int] = Field(primary_key=True)
	id_user: int = Field(foreign_key="users.id_user")
	is_active: int = Field(default=True)

	user: "User" = Relationship(back_populates="address")
	country: Country = Relationship(back_populates="address")
