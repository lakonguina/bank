from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
)

from sqlalchemy.sql import func

from app.core.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id_customer = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)

    is_active = Column(Boolean(), default=False, nullable=False)

    date_update = Column(DateTime, server_default=func.now(), onupdate=func.now())
    date_insert = Column(DateTime, server_default=func.now())
    date_close = Column(DateTime, nullable=True)
