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


class Customer(Base):
    __tablename__ = "customers"

    id_customer = Column(Integer, primary_key=True, index=True)
    id_customer_status = Column(Integer, ForeignKey("customers_status.id_customer_status"))
    customer_status = relationship("CustomerStatus")

    login = Column(String(64), nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)

    date_insert = Column(DateTime, server_default=func.now())

class CustomerStatus(Base):
    __tablename__ = "customers_status"

    id_customer_status = Column(Integer, primary_key=True, index=True)
    slug = Column(String(64), nullable=False)
