from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.database import get_session
from app.models.models import Empresa, Usuario
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class EmpresaCreate(BaseModel):
    nombre: str

class UsuarioCreate(BaseModel):
    email: str
    password: str
    empresa_id: int

@router.post("/empresa")
def crear_empresa(data: EmpresaCreate, session: Session = Depends(get_session)):
    empresa = Empresa(nombre=data.nombre)
    session.add(empresa)
    session.commit()
    session.refresh(empresa)
    return empresa

@router.post("/usuario")
def crear_usuario(data: UsuarioCreate, session: Session = Depends(get_session)):
    hashed = pwd_context.hash(data.password)
    user = Usuario(email=data.email, hashed_password=hashed, empresa_id=data.empresa_id)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
