# app/db/database.py
from sqlmodel import SQLModel, create_engine
from sqlalchemy.engine import URL
import os
from sqlmodel import Session


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/app")
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session