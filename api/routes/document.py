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
	file_selfie: UploadFile,
	file_recto: UploadFile,
	file_verso: UploadFile,
	session: Session = Depends(get_session),
	id_user: int = Depends(has_access),
):
	type_selfie = get_document_type(session, "selfie")
	type_idcard_recto = get_document_type(session, "idcard_recto")
	type_idcard_verso = get_document_type(session, "idcard_verso")

	user = get_user_by_id(session, id_user)

	db_selfie = DocumentUser(
		user=user,
		type_=type_selfie,
		filesize=file_selfie.size,
		filename=file_selfie.filename,
	)

	db_recto = DocumentUser(
		user=user,
		type_=type_idcard_recto,
		filesize=file_recto.size,
		filename=file_recto.filename,
	)

	db_verso = DocumentUser(
		user=user,
		type_=type_idcard_verso,
		filesize=file_verso.size,
		filename=file_verso.filename,
	)

	session.add(db_selfie)
	session.add(db_recto)
	session.add(db_verso)

	session.commit()

	return {"detail": "Document created with success"}
