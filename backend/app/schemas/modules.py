from pydantic import BaseModel, EmailStr
from typing import Optional

class ModuleBase(BaseModel):    
    name: str

class ModuleCreate(ModuleBase):
    name: str  

class ModuleUpdate(ModuleBase):
    name : str
    

