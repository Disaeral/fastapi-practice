from sqlalchemy.orm import Session
from typing import List
from src.infrastructure.entities import User as UserORM
from src.core.entities.user import User
from src.core.repositories import UserRepository
from src.core.mappers import Mapper
from src.infrastructure.mappers import UserMapper
from src import db

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self):
        self.session: Session = db.get_session()
        self.mapper: Mapper = UserMapper()

    def get_all(self): # should implementation return abstract or concrete?
        # it should handle the orm and return domain objects
        res:List[UserORM] = self.session.query(UserORM).all()
        mapped_res = []
        for user in res:
            mapped_res.append(self.mapper._to_domain(user))
        return 

    def get_by_id(self, id: int):
        pass

    def update(self, user: User):
        return user

    def delete(self, id: int):
        return id
    
    def create(self, user:User):
        mapped_user: UserORM = self.mapper._to_orm(user)
        created = self.session.add(mapped_user)
        self.session.commit()
        return user # self.mapper._to_domain(created)
    
