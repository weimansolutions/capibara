from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    
    username: str
    name : str
    lastname : str
    email: EmailStr
    phone : Optional[int] = None
    role_id: Optional[int] = None
    is_active : bool
    is_superadmin : bool

class UserCreate(UserBase):
    password: str  
    company_id: int 

class UserUpdate(BaseModel):
    username : Optional[str] = None
    name  : Optional[str] = None
    lastname  : Optional[str] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = None
    is_active: Optional[bool] = None
    is_superadmin: Optional[bool] = None

class UserOut(UserBase):
    id: int
    company_id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str


class ChangePassword(BaseModel):
    old_password: str
    new_password: str
