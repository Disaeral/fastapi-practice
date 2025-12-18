from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from sqlalchemy.orm import mapped_column, Mapped, Session, DeclarativeBase, sessionmaker
from sqlalchemy import VARCHAR, BIGINT, create_engine, URL
from os import getenv


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        BIGINT, primary_key=True, unique=True, autoincrement=True
    )


class User:
    def __init__(self, username, fullname, password):
        self.username: str = username
        self.fullname: str = fullname
        self.password: str = self._hash_pass(password)

    def _hash_pass(self, secret: str):
        return f"cached_{secret}"

    def validate(self):
        if len(self.username) < 5:
            raise ValueError("Username is too short")
        elif "cached_" not in self.password:
            raise ValueError("invalid password hashing")


class FastAPIUser(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(VARCHAR(30))
    password: Mapped[str] = mapped_column(VARCHAR(255))
    fullname: Mapped[Optional[str]] = mapped_column(VARCHAR(255))


E = TypeVar("E")  # e for entity
ID = TypeVar("ID")
ORM = TypeVar("ORM")

# class GenericCRUDRepo(ABC, Generic[E, ID]):
#     @abstractmethod
#     def get_all(self) -> List[E]|None:
#         pass
#     @abstractmethod
#     def get_by_id(self, id: ID) -> E|None:
#         pass
#     @abstractmethod
#     def update(self, user: E) -> E:
#         pass
#     @abstractmethod
#     def delete(self, id: ID) -> E:
#         pass


class Mapper(ABC, Generic[E, ORM]):
    @abstractmethod
    def _to_domain(self, orm: ORM) -> E:
        pass

    @abstractmethod
    def _to_orm(self, e: E) -> ORM:
        pass





class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> Optional[List[User]]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, id: int) -> User:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass


class FastAPIUserRepository(UserRepository):
    def __init__(self, session, mapper):
        self.session: Session = session
        self.mapper = mapper

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user: User):
        created = self.session.add(user)
        self.session.commit()
        return created or user

    def get_by_id(self, id: int) -> User | None:
        return self.mapper._to_domain(self.session.get_one(FastAPIUser, ident=id)) 




# user_repo = FastAPIUserRepository(session=session, mapper=mapper)
