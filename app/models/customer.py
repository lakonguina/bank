from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func

from app.db.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id_customer = Column(Integer, primary_key=True, index=True)

    email = Column(String(350), index=True, nullable=False)
    phone = Column(String(16), index=True, nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)

    is_active = Column(Boolean(), default=False, nullable=False)
    is_email_active = Column(Boolean(), default=False, nullable=False)
    is_phone_active = Column(Boolean(), default=False, nullable=False)

    date_email = Column(DateTime, server_default=func.now())
    date_phone = Column(DateTime, server_default=func.now())
    date_update = Column(DateTime, server_default=func.now(), onupdate=func.now())
    date_insert = Column(DateTime, server_default=func.now())
    date_close = Column(DateTime, nullable=True)
