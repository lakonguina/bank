from sqlmodel import Session, select

from api.schemas.country import Country


def get_country(session: Session, alpha3: str) -> Country:
	return session.exec(
		select(Country)
		.where(Country.alpha3 == alpha3)
	).first()
