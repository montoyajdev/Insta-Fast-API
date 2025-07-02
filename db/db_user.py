from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from db import models
from db.hashing import Hash

def create_user(db: Session, request: UserBase):
    new_user = models.DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
