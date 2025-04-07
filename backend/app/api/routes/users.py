from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.database import get_session
from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate, UserOut
from app.core.security import get_password_hash
from app.crud.user import get_users, create_user, update_user,get_user,get_users_all
from app.api.deps.auth import get_current_active_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/listar", status_code=status.HTTP_201_CREATED)
def list_users(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)
    ):

    return get_users(session, 1)

@router.get("/listar_todo", status_code=status.HTTP_201_CREATED)
def list_users(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)
    ):

    return get_users_all(session)

@router.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user_(
    user_in: UserCreate, 
    session: Session = Depends(get_session), 
    current_user: User = Depends(get_current_active_user)
    ):

    return create_user(user_in, session)

@router.patch("/update_user/{user_id}", response_model=UserOut)
def update_user_endpoint(
    user_id: int,
    updates: UserUpdate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_active_user)
    ):

    db_user = get_user(db, user_id, current_user.company_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return update_user(db, db_user, updates)