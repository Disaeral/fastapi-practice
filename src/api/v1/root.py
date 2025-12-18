from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags = ["test_tag"])
def index():
    return {"message": "Hello World"}