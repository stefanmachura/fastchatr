from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.orm import relationship

from app.models import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32))
    email = Column(String)
    password = Column(String)
    joined = Column(DateTime)

    posts = relationship("Post", back_populates="author")
