from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse

from sqlmodel import Session, select

from backoffice.core.database import get_session_frontoffice
from backoffice.core.settings import settings
from backoffice.core.templates import templates

from backoffice.schemas.frontoffice.user import UserFrontoffice
from backoffice.schemas.backoffice.user import UserBackoffice
from backoffice.routes.auth import manager


router = APIRouter(tags=["Users"])

@router.get("/user/list")
def list_user(
	request: Request,
	session: Session = Depends(get_session_frontoffice),
	_ = Depends(manager),
):
	users = session.exec(
		select(UserFrontoffice)
		.order_by(UserFrontoffice.id_user.desc())
	).all()

	context = {
		"request": request,
		"users": users,
	}

	return templates.TemplateResponse("user/user_list.html", context)

@router.get("/user/{id_user}")
def user_detail(
	id_user: int,
	request: Request,
	session: Session = Depends(get_session_frontoffice),
	_ = Depends(manager),
):
	user = session.exec(
		select(UserFrontoffice)
		.where(UserFrontoffice.id_user == id_user)
	).first()

	if not user:
		return RedirectResponse("/user/list", status_code=303)

	user = session.exec(
		select(UserFrontoffice)
		.where(UserFrontoffice.id_user == id_user)
	).first()
	
	context = {
		"request": request,
		"user": user, 
	}

	return templates.TemplateResponse("user/user_detail.html", context)
