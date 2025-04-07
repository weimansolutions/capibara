from pydantic import BaseModel, EmailStr
from typing import Optional

class PermissionsBase(BaseModel):
    name: str
    description: str
    module_id: int

class PermissionsCreate(PermissionsBase):
    name: str
    description: str
    module_id: int 

class PermissionsUpdate(BaseModel):
    
    name  : Optional[str] = None
    description: Optional[str] = None
    module_id: Optional[int] = None
    

class PermissionsOut(PermissionsBase):
    id: int
    module_id: int

    class Config:
        orm_mode = True

