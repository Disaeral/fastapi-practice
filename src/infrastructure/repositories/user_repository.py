from sqlalchemy.orm import Session
from typing import List, Callable
from src.core.entities.user import User
from src.infrastructure.entities import User as UserORM
from src.core.repositories import UserRepository
from src.core.mappers import Mapper
from src.infrastructure.mappers import UserMapper


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session_factory):
        self.session_factory: Callable[..., Session] = session_factory
        self.mapper: Mapper = UserMapper()
    def get_all(self):
        with self.session_factory() as session:
            res: List[UserORM] = session.query(UserORM).all()
            return [self.mapper._to_domain(user) for user in res]

    def create(self, user):
        with self.session_factory() as session:
            mapped_user: UserORM = self.mapper._to_orm(user)
            session.add(mapped_user)
            session.commit()
            return self.mapper._to_domain(mapped_user)

    def get_by_id(self, id: int):
        with self.session_factory() as session:
            res: UserORM | None = session.query(UserORM).filter(UserORM.id == id).first()
            if res is not None:
                return self.mapper._to_domain(res)
    
    def get_by_username(self, username: str) -> User | None:
        with self.session_factory() as session:
            entity = session.query(UserORM).where(UserORM.username == username).first()
            if entity:
                return self.mapper._to_domain(entity)

    def update(self, id, user):
        with self.session_factory() as session:
            candidate = session.query(UserORM).filter(UserORM.id == id).first()
            if candidate:
                candidate.fullname = user.fullname if user.fullname else candidate.fullname
                candidate.username = user.username if user.username else candidate.username
                candidate.password = user.password if user.password else candidate.password
                candidate.is_banned = user.is_banned if user.is_banned else candidate.is_banned
                session.commit()
                return self.mapper._to_domain(candidate)

    def delete(self, id: int):
        with self.session_factory() as session:
            query = session.query(UserORM).filter(UserORM.id == id)
            candidate = query.first()
            print(candidate)
            if candidate is not None:
                session.delete(candidate)
                session.commit()
                if len(query.all()) == 0:
                    return id
                else:
                    return 0
            else:
                return 0
