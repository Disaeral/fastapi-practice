from fastapi import APIRouter
from src.api.v1 import posts, users, root

router = APIRouter(prefix="/v1")
router.include_router(posts.router)
router.include_router(users.router)
router.include_router(root.router)
