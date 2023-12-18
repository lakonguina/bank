from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile

from sqlmodel import Session

from api.core.database import get_session

from api.dependencies.security import has_access

from api.schemas.detail import Detail
from api.schemas.document import DocumentUser

from api.crud.document import get_document_type, get_document_by_id_user
from api.crud.user import get_user_by_id



router = APIRouter(tags=["Documents"])

@router.post("/user/document/create", response_model=Detail)
def document_user_create(
	file: UploadFile,
	type_ = Form(),
	session: Session = Depends(get_session),
	id_user: int = Depends(has_access),
):
	type_ = get_document_type(session, type_)
	
	if not type_:
		raise HTTPException(
			status_code=400,
			detail="Document type do not exist"
		)
	
	db_document = get_document_by_id_user(session, id_user)
	
	if db_document:
		raise HTTPException(
			status_code=400,
			detail="User already have a document"
		)

	user = get_user_by_id(session, id_user)

	db_document = DocumentUser(
		user=user,
		type_=type_,
		filesize=file.size,
		filename=file.filename,
	)

	session.add(db_document)
	session.commit()

	return {"detail": "Document created with success"}
