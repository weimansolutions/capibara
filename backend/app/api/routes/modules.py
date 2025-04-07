from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.database import get_session
from app.models.modules import Module
from app.schemas.modules import ModuleCreate, ModuleUpdate
from app.api.deps.auth import get_current_active_user
from app.models.users import User


router = APIRouter(prefix="/modules", tags=["Modules"])

@router.post("/create_module", status_code=status.HTTP_201_CREATED)
def create_module(
    module_in: ModuleCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)):

    module = Module(
        name=module_in.name
    )
    session.add(module)
    session.commit()
    session.refresh(module)
    return {"message": "Modulo creado correctamente", "id": module.id}

@router.get("/view_modules", status_code=status.HTTP_201_CREATED)
def get_modules(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)):

    return session.query(Module).all()