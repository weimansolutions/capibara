# app/crud/users.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import models, schemas
from app.core.security import get_password_hash

# Obtener todos los usuarios existentes
def get_users_all(db: Session):
    return db.query(models.User).all()

# Obtener todos los usuarios de una empresa
def get_users(db: Session, company_id: int):
    return db.query(models.User).filter(models.User.company_id == company_id).all()

# Obtener usuario por ID (y empresa)
def get_user(db: Session, user_id: int, company_id: int):
    return db.query(models.User).filter(models.User.id == user_id, models.User.company_id == company_id).first()

# Obtener usuario por username (general, para login)
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Crear usuario nuevo
def create_user(user_in: schemas.users.UserCreate, session: Session):
   
    existing_user = session.query(models.User).filter(models.User.email == user_in.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya está registrado"
        )

    user = models.User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        company_id=user_in.company_id,
        role_id=user_in.role_id,
        is_active=True,
        username = user_in.username,
        name = user_in.name,
        lastname = user_in.lastname,
        phone = user_in.phone,
        is_superadmin = False 

    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": "Usuario creado correctamente", "id": user.id}

# Actualizar usuario existente
def update_user(db: Session, db_user: models.User, updates: schemas.users.UserUpdate):
    for field, value in updates.dict(exclude_unset=True).items():
        if field == "password":
            setattr(db_user, "hashed_password", get_password_hash(value))
        else:
            setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# Eliminar usuario (borrado duro)
def delete_user(db: Session, db_user: models.User):
    db.delete(db_user)
    db.commit()
    return True
