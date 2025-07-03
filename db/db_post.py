from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from routers.schemas import PostBase
from db.models import DbPost
from datetime import datetime

def create_post(db:Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.now(),
        user_id = request.creator_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post