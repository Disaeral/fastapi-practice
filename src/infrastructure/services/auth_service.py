from datetime import datetime
from typing import List, Optional
from src.core.dto.user import LoginUserDTO
from src.core.repositories import UserRepository
from src.core.entities.user import User
from src.core.services import UserService
from src.infrastructure.helpers.hash_password import hash_sha265

class FastAPIAuthService(UserService):
    def __init__(self, user_repo: UserRepository) -> None:
        self.repository = user_repo