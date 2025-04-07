from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.database import get_session
from app.models.role import Role
from app.schemas.role import RolCreate, RolUpdate
from app.api.deps.auth import get_current_active_user
from app.models.users import User


router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/create_role", status_code=status.HTTP_201_CREATED)
def create_role(
    role_in: RolCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)
    ):

    rol = Role(
        name=role_in.name,
        company_id=role_in.company_id
    )
    session.add(rol)
    session.commit()
    session.refresh(rol)
    return {"message": "Rol creado correctamente", "id": rol.id}

@router.get("/view_roles", status_code=status.HTTP_201_CREATED)
def get_roles(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)):

    return session.query(Role).all()