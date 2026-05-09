from fastapi import APIRouter
from src.core.dto import LoginUserDTO
from src.infrastructure.services import FastAPIUserService
from dishka.integrations.fastapi import FromDishka, DishkaRoute

router = APIRouter(prefix="/auth", route_class=DishkaRoute)

@router.post("/login", tags = ["auth", "users"])
def login_user(user: LoginUserDTO, user_service: FromDishka[FastAPIUserService]):
    return user_service.login_user(user)
