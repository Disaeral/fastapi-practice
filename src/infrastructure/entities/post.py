from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import BIGINT, VARCHAR, ForeignKey
from base import Base
from mixins import Timestamp

class Post(Base, Timestamp):
    __tablename__ = "posts"
    title: Mapped[str]   = mapped_column(VARCHAR(200))
    body: Mapped[str]    = mapped_column(VARCHAR(1024))
    user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users.id", ondelete="SET NULL"))
    user = relationship("User", back_populates="posts")