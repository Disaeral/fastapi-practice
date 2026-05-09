from abc import ABC, abstractmethod
from typing import Optional
from ..dto import LoginUserDTO

class AuthService(ABC):
    @abstractmethod
    def login_user(self, user: LoginUserDTO) -> Optional[str]:
        pass

