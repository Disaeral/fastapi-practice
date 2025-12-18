from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import BIGINT

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True, autoincrement=True)