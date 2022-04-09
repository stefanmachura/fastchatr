import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

passw = os.getenv("POSTGRES_PASSWORD")
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{passw}@db/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
