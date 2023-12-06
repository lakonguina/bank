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


class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)

    id_user_status = Column(Integer, ForeignKey("users_status.id_user_status"))
    user_status = relationship("UserStatus")

    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    date_insert = Column(DateTime, server_default=func.now())


class UserStatus(Base):
    __tablename__ = "users_status"

    id_user_status = Column(Integer, primary_key=True, index=True)
    slug = Column(String(64), nullable=False)
