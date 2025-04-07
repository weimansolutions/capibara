from pydantic import BaseModel, EmailStr
from typing import Optional

class RolBase(BaseModel):
    name: str
    company_id : int

class RolCreate(RolBase):
    name: str
    company_id: int 

class RolUpdate(BaseModel):
    
    name  : Optional[str] = None
    company_id: Optional[int] = None
    

class RolOut(RolBase):
    id: int
    company_id: int

    class Config:
        orm_mode = True

