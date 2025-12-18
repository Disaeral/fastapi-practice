from fastapi import APIRouter

router = APIRouter(prefix="/posts")

@router.get("/", tags = ["posts", "list"])
def index():
    return {"message": "all posts", "posts": []}

@router.post("/", tags=["posts", "create"])
def create_post(postBody):
    return postBody

@router.delete("/{id}", tags=["posts", "delete"])
def delete_post(postId: int):
    return {"message": f"post {postId} successfully deleted"}

@router.patch("/{id}", tags=["posts", "update"])
def update_post(postId: int):
    return {"message": f"post {postId} successfully updated"}