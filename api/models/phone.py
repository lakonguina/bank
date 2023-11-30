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


class Phone(Base):
    __tablename__ = "phones"

    id_phone= Column(Integer, primary_key=True, index=True)
    id_customer = Column(Integer, ForeignKey("customers.id_customer"))

    phone = Column(String(16), nullable=False)
    is_active = Column(Boolean(), default=True, nullable=False)
    is_phone_active = Column(Boolean(), default=False, nullable=False)

    date_validation= Column(DateTime)
    date_insert = Column(DateTime, server_default=func.now(), nullable=False)
