from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.crud import create_post, get_all_posts, get_db
from app.models.schemas import PostBase

router = APIRouter()


@router.get("/", response_model=List[PostBase])
async def get_posts(db: Session = Depends(get_db)):
    return get_all_posts(db)


@router.post("/{author_id}")
async def new_post(author_id: int, db: Session = Depends(get_db)):
    return create_post(db, author_id)
