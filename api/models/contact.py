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

from api.core.base import Base


class Contact(Base):
    __tablename__ = "contacts"

    id_contact = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id_user"))

    phone = Column(String(16), index=True, nullable=False)
    is_phone_active = Column(Boolean(), default=False, nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)

    date_phone = Column(DateTime, server_default=func.now())
    date_insert = Column(DateTime, server_default=func.now())
