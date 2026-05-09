from datetime import datetime
from typing import List, Optional
from src.core.repositories import UserRepository
from src.core.entities.user import User
from src.core.services import UserService
from src.infrastructure.helpers.hash_password import hash_sha265

class FastAPIUserService(UserService):
    def __init__(self, user_repo: UserRepository) -> None:
        self.repository = user_repo

    def create_user(self, user) -> User:
        user.password = hash_sha265(user.password)
        return self.repository.create(user)
    
    def update_user(self, id, user) -> Optional[User]:
        return self.repository.update(id, user)
    
    def get_all_users(self) -> Optional[List[User]]:
        return self.repository.get_all()
    
    def get_user_by_id(self, id: int) -> Optional[User]:
        return self.repository.get_by_id(id)
    
    def delete_user(self, id: int) -> int:
        return self.repository.delete(id)
    
    def get_all_users_registered_after(self, date: datetime) -> Optional[List[User]]:
        return
