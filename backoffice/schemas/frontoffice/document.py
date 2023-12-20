from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class DocumentStatus(SQLModel, table=True):
	__tablename__ = "documents_status"

	id_document_status: int = Field(primary_key=True)
	slug: str

	documents: list["DocumentUser"] = Relationship(back_populates="status")


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
	id_document_status: int = Field(foreign_key="documents_status.id_document_status")
	
	filesize: int
	filename: str
	
	type_: DocumentUserType = Relationship(back_populates="documents")
	status: DocumentStatus= Relationship(back_populates="documents")
	user: "UserFrontoffice" = Relationship(back_populates="documents")

	date_insert: datetime
