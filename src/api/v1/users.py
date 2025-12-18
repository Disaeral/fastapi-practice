from fastapi import APIRouter
from src.infrastructure.services import FastAPIUserService

router = APIRouter(prefix="/users")

@router.get("/", tags = ["users"])
def get_all_users():
    return FastAPIUserService().get_all_users()

@router.post("/", tags = ["users"])
def create_user(user):
    return user

@router.delete("/{id}", tags= ["users"])
def delete_user(userId):
    return userId

@router.patch("/{id}", tags = ["users"])
def update_user(user):
    return user