from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.database import get_session
from app.models.users import User
from app.schemas.users import UserCreate
from app.core import security 
from app.crud.user import get_user_by_username
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Login"])

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_session)
    ):

    user = get_user_by_username(db, form_data.username)
    
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key="token",
        value=access_token,
        httponly=True,  # evita que JS lea la cookie
        secure=False,   # ponelo en True si usás HTTPS
        samesite="Lax",
        max_age=60 * 60,  # 1 hora
        path="/"
    )
    
    return response

@router.post("/logout")
def logout():
    response = JSONResponse(content={"message": "Logout successful"})
    response.delete_cookie(key="token", path="/")  # Borra la cookie
    return response