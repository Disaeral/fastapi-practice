from sqlalchemy.orm import Session
from typing import List
from src.infrastructure.entities import User as UserORM
from src.core.entities.user import User
from src.core.repositories import UserRepository
from src.core.mappers import Mapper
from src.infrastructure.mappers import UserMapper
from src.infrastructure import db


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self):
        self.session: Session = db.get_session()
        self.mapper: Mapper = UserMapper()

    def get_all(self):
        res: List[UserORM] = self.session.query(UserORM).all()
        return [self.mapper._to_domain(user) for user in res]

    def create(self, user: User):
        mapped_user: UserORM = self.mapper._to_orm(user)
        self.session.add(mapped_user)
        self.session.commit()
        return self.mapper._to_domain(mapped_user)

    def get_by_id(self, id: int):
        res: UserORM | None = self.session.query(UserORM).filter(UserORM.id == id).first()
        if res is not None:
            return self.mapper._to_domain(res)

    def update(self, user: User):
        return user

    def delete(self, id: int):
        return id
