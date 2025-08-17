from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:monu1234@localhost:5432/ai_resume")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        