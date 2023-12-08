from datetime import timedelta
from pydantic import EmailStr

from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.responses import RedirectResponse, Response
from fastapi_login import LoginManager

from sqlmodel import Session, select

from backoffice.core.database import get_session_backoffice, engine_backoffice
from backoffice.core.settings import settings
from backoffice.core.templates import templates
from backoffice.core.manager import manager

from backoffice.dependencies.security import get_password_hash, verify_password

from backoffice.schemas.backoffice.user import UserBackoffice


router = APIRouter(tags=["Authentication"])

@manager.user_loader()
def load_user(id_user: int):
	"""
	Get 'sub' argument of the cookie that correspond to "id_user_internal"
	"""
	with Session(engine_backoffice) as session:
		user = session.get(UserBackoffice, id_user)

	return user

@router.get("/")
def login(request: Request):
	if request.state.user:
		return RedirectResponse('/user/list', status_code=303)

	context = {"request": request}
	return templates.TemplateResponse("auth/login.html", context)


@router.post("/")
def login(
	request: Request,
	response: Response,
	email: EmailStr = Form(),
	password: str = Form(),
	session: Session = Depends(get_session_backoffice),
):
	user = session.exec(select(UserBackoffice).where(UserBackoffice.email == email)).first()	
	
	context = {"request": request}

	if not user:
		context["message"] = "Email invalid."
		return templates.TemplateResponse("auth/login.html", context)
	
	password_valid = verify_password(password, user.password)		

	if not password_valid:
		context["message"] = "Password invalid."
		return templates.TemplateResponse("auth/login.html", context)

	# Set cookie
	token = manager.create_access_token(
		data={"sub": user.id_user_internal},
		expires=timedelta(hours=24)
	)
	
	manager.set_cookie(response, token)

	# GET redirection
	response.status_code = 303
	response.headers["location"] = '/user/list'

	return response

@router.get("/signout")
def login(response: Response):

	response.status_code = 303
	response.headers["location"] = '/'

	manager.set_cookie(response, None)

	return response
