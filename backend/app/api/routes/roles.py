from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.database import get_session
from app.models.role import Role
from app.schemas.role import RolCreate, RolUpdate
from app.api.deps.auth import require_superadmin
from app.models.users import User
from app.schemas.associations import RolePermissionLink
from app.crud.associations import assign_permission_to_role




router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/assign-permissions", dependencies=[Depends(require_superadmin)])
def assign_permissions(data: RolePermissionLink, db: Session = Depends(get_session)):
    return assign_permission_to_role(db, data.permission_id, data.role_id)

@router.post("/create_role", status_code=status.HTTP_201_CREATED)
def create_role(
    role_in: RolCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(require_superadmin)
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
    current_user: User = Depends(require_superadmin)):

    return session.query(Role).all()