from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .usuario import Usuario

class Perfil(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    empresa_id: int = Field(foreign_key="empresa.id")

    usuarios: List["Usuario"] = Relationship(back_populates="perfil")
