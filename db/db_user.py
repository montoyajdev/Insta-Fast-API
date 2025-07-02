from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from db import models

def create_user(db: Session, request: UserBase):
    new_user = models.DbUser(
        username=request.username,
        email=request.email,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
