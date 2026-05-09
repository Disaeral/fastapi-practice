from abc import ABC, abstractmethod
from typing import Optional, List
from datetime import datetime
from ..entities.user import User
from ..dto import CreateUserDTO, UpdateUserDTO, LoginUserDTO

class UserService(ABC):
    @abstractmethod
    def get_all_users(self) -> Optional[List[User]]:
        pass

    @abstractmethod
    def get_user_by_id(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def update_user(self, id: int, user: UpdateUserDTO) -> Optional[User]:
        pass

    @abstractmethod
    def delete_user(self, id: int) -> int:
        pass

    @abstractmethod
    def create_user(self, user: CreateUserDTO) -> User:
        pass

    @abstractmethod
    def login_user(self, user: LoginUserDTO) -> None | str:
        pass

    @abstractmethod
    def get_all_users_registered_after(self, date: datetime) -> Optional[List[User]]:
        pass
