from sqlmodel import Field, Relationship, SQLModel


class DocumentUserTypeSlug(SQLModel):
	slug: str = Field(max_length=32)


class DocumentUserType(DocumentUserTypeSlug, table=True):
	__tablename__ = "documents_users_type"

	id_document_user_type: int = Field(primary_key=True)
	documents: list["DocumentUser"] = Relationship(back_populates="type_")


class DocumentUser(SQLModel, table=True):
	__tablename__ = "documents_users"

	id_document: int | None = Field(primary_key=True)

	id_user: int = Field(foreign_key="users.id_user")
	id_document_user_type: int = Field(foreign_key="documents_users_type.id_document_user_type")

	is_valid: bool = Field(default=False)

	type_: DocumentUserType = Relationship(back_populates="documents")
	user: "User" = Relationship(back_populates="document")
