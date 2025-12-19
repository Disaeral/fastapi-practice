from fastapi import APIRouter
from src.infrastructure.services import FastAPIUserService
from src.api.schemas import CreateUserSchema

router = APIRouter(prefix="/users")

@router.get("/", tags = ["users"])
def get_all_users():
    return FastAPIUserService().get_all_users()

@router.get("/{id}", tags = ["users"])
def get_user_by_id(id: int):
    return FastAPIUserService().get_user_by_id(id)

@router.post("/", tags = ["users"])
def create_user(user: CreateUserSchema):
    print(user, "user recieved")
    return user

@router.delete("/{id}", tags= ["users"])
def delete_user(userId):
    return userId

@router.patch("/{id}", tags = ["users"])
def update_user(user):
    return user