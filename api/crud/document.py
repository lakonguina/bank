from sqlmodel import Session, select

from api.schemas.document import DocumentStatus, DocumentUser, DocumentUserType


def get_document_status(session: Session, slug: str) -> DocumentStatus:
	return session.exec(
		select(DocumentStatus)
		.where(DocumentStatus.slug == slug)
	).one()

def get_document_type(session: Session, slug: str) -> DocumentUserType:
	return session.exec(
		select(DocumentUserType)
		.where(DocumentUserType.slug == slug)
	).first()

def get_document_by_id_user(session: Session, id_user: int) -> DocumentUser:
	return session.exec(
		select(DocumentUser)
		.where(DocumentUser.id_user == id_user)
	).first()
