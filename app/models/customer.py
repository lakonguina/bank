from sqlalchemy import Boolean, Column, Integer, String

from app.db.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id_customer = Column(Integer, primary_key=True, index=True)
    phone = Column(String, index=True, nullable=True)
    email = Column(String, index=True, nullable=False)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    password = Column(String, nullable=True)
    is_active = Column(Boolean(), default=True)
    is_phone_active = Column(Boolean(), default=True)
    is_email_active = Column(Boolean(), default=True)
