from typing import List, Optional
from abc import abstractmethod, ABC
from ..entities.user import User

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
    def delete(self, id: int) -> int:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass
