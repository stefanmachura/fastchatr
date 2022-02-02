from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

from sqlalchemy.orm import relationship

from app.models import Base

from app.models.user import User

# from app.models.user import User


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    added = Column(DateTime)
    body = Column(String, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    author = relationship("User", back_populates="posts")
