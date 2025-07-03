from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_post import create_post
from routers.schemas import PostBase, PostDisplay
from fastapi import HTTPException, status

router = APIRouter(
    prefix = "/post",
    tags = ["post"]
)

image_url_types = ["absolute", "relative"]

@router.post("/", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
        detail="Parameter image_url_type can only be absolute or relative")
    return create_post(db, request)