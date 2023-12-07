from fastapi import APIRouter, Request, Depends

from sqlmodel import Session, select

from backoffice.core.database import engine, get_session
from backoffice.core.settings import settings

from backoffice.schemas.user import User

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="backoffice/templates")

router = APIRouter(tags=["Users"])

@router.get("/list/user")
def list_user(
	request: Request,
	session: Session = Depends(get_session)
):
	users = session.exec(select(User)).all()

	return templates.TemplateResponse("list_user.html", {"users": users, "request": request})
