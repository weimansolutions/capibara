from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.database import get_session
from app.models.permissions import Permission
from app.schemas.permission import PermissionsCreate, PermissionsUpdate
from app.api.deps.auth import get_current_active_user
from app.models.users import User


router = APIRouter(prefix="/permission", tags=["Permission"])

@router.post("/create_permission", status_code=status.HTTP_201_CREATED)
def create_permission(
    permission_in: PermissionsCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)):

    permission = Permission(
        name=permission_in.name,
        description=permission_in.description,
        module_id=permission_in.module_id
    )
    session.add(permission)
    session.commit()
    session.refresh(permission)
    return {"message": "Permission creado correctamente", "id": permission.id}

@router.get("/view_permission", status_code=status.HTTP_201_CREATED)
def get_permission(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)
    ):
    return session.query(Permission).all()