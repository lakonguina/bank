from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile

from sqlmodel import Session

from api.core.database import get_session
from api.dependencies.security import has_access

from api.schemas.detail import Detail



router = APIRouter(tags=["Documents"])

@router.post("/user/document/create", response_model=Detail)
def document_user_create(
	file: UploadFile,
	type_ = Form(),
	session: Session = Depends(get_session),
	id_user: int = Depends(has_access),
):
	return {"detail": "Document created with success"}
