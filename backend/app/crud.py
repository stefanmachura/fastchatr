from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.post import Post
from app.models.user import User

from app.models.schemas import UserCreate

from app.database import SessionLocal


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_all_posts(db: Session):
    return db.query(Post).all()


def create_post(db: Session, author_id: int):
    db_item = Post(body="omg", user_id=author_id)
    db.add(db_item)
    db.commit()


def get_single_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: UserCreate):
    db_item = User(username=user.username, email=user.email, password=user.password)
    db.add(db_item)
    db.commit()
    return db_item


def search_users_by_username(db: Session, username_query: str):
    username_query = f"%{username_query}%"
    return db.query(User).filter(User.username.like(username_query)).all()
