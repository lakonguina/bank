from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse

from sqlmodel import Session, select

from backoffice.core.database import get_session_frontoffice
from backoffice.core.templates import templates

from backoffice.schemas.frontoffice.user import UserFrontoffice, UserStatus
from backoffice.schemas.frontoffice.email import Email
from backoffice.schemas.frontoffice.phone import Phone
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

	emails = session.exec(
		select(Email)
		.where(Email.id_user == id_user)
	).all()

	phones = session.exec(
		select(Phone)
		.where(Phone.id_user == id_user)
	).all()
	
	context = {
		"emails": emails, 
		"phones": phones, 
		"request": request,
		"user": user, 
	}

	return templates.TemplateResponse("user/user_detail.html", context)

@router.get("/user/validate/{id_user}")
def user_validate(
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

	status = session.exec(
		select(UserStatus)
		.where(UserStatus.slug == "valid")
	).one()
	
	user.status = status
	
	session.add(user)
	session.commit()

	return RedirectResponse(f"/user/{id_user}", status_code=303)
