from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class CountryIn(SQLModel):
	alpha3: str = Field(primary_key=True, min_length=3, max_length=3)


class CountryOut(CountryIn):
	name: str


class Country(CountryOut, table=True):
	__tablename__ = "countries"

	user: "User" = Relationship(back_populates="country")
	address: "Address" = Relationship(back_populates="country")
