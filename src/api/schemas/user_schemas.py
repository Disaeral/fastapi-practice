from pydantic import BaseModel
from src.core.entities.user import User

class CreateUserSchema(BaseModel, User):
    pass
