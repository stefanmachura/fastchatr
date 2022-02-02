from typing import List, Optional
import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class PostBase(BaseModel):
    id: int
    added: Optional[datetime.datetime]
    body: Optional[str]
    author: Optional[UserBase]

    class Config:
        orm_mode = True


class PostShort(BaseModel):
    body: Optional[str]

    class Config:
        orm_mode = True


class UserPostList(BaseModel):
    id: int
    username: str
    email: Optional[str]
    posts: Optional[List[PostShort]]

    class Config:
        orm_mode = True


class UsernameOnly(BaseModel):
    username: str

    class Config:
        orm_mode = True
