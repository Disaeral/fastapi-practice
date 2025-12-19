from datetime import datetime
from typing import List
from src.core.repositories import UserRepository
from src.core.entities.user import User
from src.core.services import UserService
from src.infrastructure.repositories import SQLAlchemyUserRepository

class FastAPIUserService(UserService):
    def __init__(self) -> None:
        self.repository:UserRepository = SQLAlchemyUserRepository()

    def create_user(self, user: User) -> User:
        return self.repository.create(user)
    
    def update_user(self, user: User) -> User:
        return user
    
    def get_all_users(self) -> List[User] | None:
        return self.repository.get_all()
    
    def get_user_by_id(self, id: int) -> User | None:
        return self.repository.get_by_id(id)
    
    def delete_user(self, id: int) -> int:
        return id
    
    def get_all_users_registered_after(self, date: datetime) -> List[User] | None:
        return 