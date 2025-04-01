from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.models import Usuario
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
import os

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginInput(BaseModel):
    email: str
    password: str

@router.post("/login", response_model=Token)
def login(data: LoginInput, session: Session = Depends(get_session)):
    user = session.exec(select(Usuario).where(Usuario.email == data.email)).first()
    if not user or not pwd_context.verify(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": user.email}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}