from pydantic import BaseModel

class UserDTO(BaseModel):
    fullname: str
    username: str
    password: str
    is_banned: bool = False

class CreateUserDTO(BaseModel):
    fullname: str
    username: str
    password: str
    is_banned: bool = False

class UpdateUserDTO(BaseModel):
    fullname: str
    username: str
    password: str
    is_banned: bool
