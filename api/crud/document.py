from sqlmodel import Session, select

from api.schemas.document import DocumentUserType


def get_document_type(session: Session, slug: str) -> DocumentUserType:
	return session.exec(
		select(DocumentUserType)
		.where(DocumentUserType.slug == slug)
	).one()
