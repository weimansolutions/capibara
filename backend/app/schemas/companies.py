from pydantic import BaseModel, EmailStr
from typing import Optional

class CompanyBase(BaseModel):    
    name: str

class CompanyCreate(CompanyBase):
    name: str  

class CompanyUpdate(CompanyBase):
    name : str
    

