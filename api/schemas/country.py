from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class CountryIn(SQLModel):
	alpha3: str = Field(primary_key=True, min_length=3, max_length=3)


class Country(CountryIn, table=True):
	__tablename__ = "countries"

	name: str

	user: "User" = Relationship(back_populates="country")
	address: "Address" = Relationship(back_populates="country")
