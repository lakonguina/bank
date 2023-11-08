from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import relationship

from app.core.base import Base


class Email(Base):
    __tablename__ = "emails"

    id_email= Column(Integer, primary_key=True, index=True)
    id_customer = Column(Integer, ForeignKey("customers.id_customer"))

    email = Column(String(16), nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)
    is_email_active = Column(Boolean(), default=False, nullable=False)

    date_validation= Column(DateTime)
    date_insert = Column(DateTime)
