from sqlmodel import SQLModel, Field
from typing import Optional

class Rol(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    empresa_id: int = Field(foreign_key="empresa.id")
