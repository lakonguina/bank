from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.base import Base


class Country(Base):
    __tablename__ = "countries"

    id_country = Column(Integer, primary_key=True, index=True)
    alpha2 = Column(String(16), nullable=False)
    alpha3 = Column(String(16), nullable=False)
    indicative = Column(String(3), nullable=False)
    name = Column(String(127), nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)
    date_insert = Column(DateTime, server_default=func.now())
