from fastapi import APIRouter, Depends

from sqlmodel import Session, select

from api.core.database import get_session

from api.schemas.country import Country


router = APIRouter(tags=["Countries"])

@router.get("/countries", response_model=list[Country])
def user_register(session: Session = Depends(get_session)):
	return session.exec(select(Country)).all()
