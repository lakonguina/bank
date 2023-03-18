from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id_customer = Column(Integer, primary_key=True, index=True)
    id_country = Column(Integer, ForeignKey("countries.id_country"))
    country = relationship("Country")

    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)

    is_active = Column(Boolean(), default=True, nullable=False)
    date_insert = Column(DateTime, server_default=func.now())
