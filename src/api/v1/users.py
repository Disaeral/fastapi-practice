from fastapi import APIRouter
from src.core.dto import CreateUserDTO, UpdateUserDTO, UserDTO
from src.infrastructure.services import FastAPIUserService
from dishka.integrations.fastapi import FromDishka, DishkaRoute

router = APIRouter(prefix="/users", route_class=DishkaRoute)

@router.get("/", tags = ["users"])
def get_all_users(user_service: FromDishka[FastAPIUserService]):
    return user_service.get_all_users()

@router.get("/{id}", tags = ["users"])
def get_user_by_id(id: int, user_service: FromDishka[FastAPIUserService]):
    return user_service.get_user_by_id(id)

@router.post("/", tags = ["users"])
def create_user(
    user: CreateUserDTO,
    user_service: FromDishka[FastAPIUserService]
):
    print(user, "user recieved")
    return user_service.create_user(user)

@router.delete("/{id}", tags = ["users"])
def delete_user(id: int, user_service: FromDishka[FastAPIUserService]):
    return user_service.delete_user(id)

@router.patch("/{id}", tags = ["users"])
def update_user(id: int, user: UpdateUserDTO, user_service: FromDishka[FastAPIUserService]):
    return user_service.update_user(id, user)