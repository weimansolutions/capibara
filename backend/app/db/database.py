from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os
from typing import Generator

# Leer la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/app")

# Crear el engine
engine = create_engine(DATABASE_URL, echo=True)

# Crear la clase Base para modelos
Base = declarative_base()

# Crear el session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency para FastAPI
def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear las tablas
def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
