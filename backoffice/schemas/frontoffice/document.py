from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class DocumentUserType(SQLModel, table=True):
	__tablename__ = "documents_users_type"

	id_document_user_type: int = Field(primary_key=True)
	slug: str

	documents: list["DocumentUser"] = Relationship(back_populates="type_")


class DocumentUser(SQLModel, table=True):
	__tablename__ = "documents_users"

	id_document: int = Field(primary_key=True)
	id_user: int = Field(foreign_key="users.id_user")
	id_document_user_type: int = Field(foreign_key="documents_users_type.id_document_user_type")
	
	filesize: int
	filename: str
	
	is_valid: bool

	type_: DocumentUserType = Relationship(back_populates="documents")
	user: "UserFrontoffice" = Relationship(back_populates="documents")

	date_insert: datetime
