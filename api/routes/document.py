from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile

#from sqlalchmey import or_
from sqlmodel import Session, select

from api.core.database import get_session

from api.dependencies.security import has_access

from api.schemas.detail import Detail
from api.schemas.document import DocumentStatus, DocumentUser, DocumentUserType

from api.crud.document import get_document_type, get_document_by_id_user, get_document_status
from api.crud.user import get_user_by_id


router = APIRouter(tags=["Documents"])

@router.post("/user/document/create", response_model=None)
def document_user_create(
	file: UploadFile,
	type_: Annotated[str, Form()],
	session: Session = Depends(get_session),
	id_user: int = Depends(has_access),
):
	type_ = get_document_type(session, type_)
	
	if not type_:
		raise HTTPException(
			status_code=400,
			detail="Document type do not exist"
		)
	
	status_awaiting = get_document_status(session, "awaiting")
	status_valid = get_document_status(session, "valid")

	db_document = session.exec(
		select(DocumentUser)
		.where((DocumentUser.status == status_awaiting) | (DocumentUser.status == status_valid))
	).first()

	if db_document:
		raise HTTPException(
			status_code=400,
			detail="Document already uploaded"
		)

	user = get_user_by_id(session, id_user)

	db_document = DocumentUser(
		user=user,
		status=status_awaiting,
		type_=type_,
		filesize=file.size,
		filename=file.filename,
	)

	session.add(db_document)
	session.commit()

	return {"detail": "Document created with success"}
