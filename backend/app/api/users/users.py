from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import crud


from app.models.schemas import UserBase, UserCreate, UserPostList, UsernameOnly


router = APIRouter()


@router.post("/new", response_model=UserBase)
async def create_user(user: UserCreate, db: Session = Depends(crud.get_db)):
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


@router.get("/search", response_model=List[UsernameOnly])
async def search_users_by_username(
    username_query: str, db: Session = Depends(crud.get_db)
):
    return crud.search_users_by_username(db, username_query)


@router.get("/{user_id}", response_model=UserPostList)
async def get_single_user(user_id: int, db: Session = Depends(crud.get_db)):
    return crud.get_single_user(db, user_id)


@router.get("/", response_model=List[UserBase])
async def get_all_users(db: Session = Depends(crud.get_db)):
    return crud.get_all_users(db)
