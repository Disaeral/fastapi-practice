from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import VARCHAR, select
from base import Base
from mixins import Timestamp

class User(Base, Timestamp):
    __tablename__ = "users"
    username: Mapped[str]           = mapped_column(VARCHAR(30))
    password: Mapped[str]           = mapped_column(VARCHAR(255))
    fullname: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    posts = relationship("Post", back_populates="user")
