from sqlmodel import SQLModel, Field
from typing import Optional

class Tarea(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    descripcion: Optional[str] = None
    estado: str = "pendiente"
    usuario_id: int = Field(foreign_key="usuario.id")
