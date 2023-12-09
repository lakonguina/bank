from sqlmodel import Field, Relationship, SQLModel


class Country(SQLModel, table=True):
	__tablename__ = "countries"

	alpha3: str = Field(primary_key=True)
	name: str

	user: "UserFrontoffice" = Relationship(back_populates="country")
	address: "Address" = Relationship(back_populates="country")
