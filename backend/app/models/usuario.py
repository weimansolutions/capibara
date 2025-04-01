from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .empresa import Empresa
    from .perfil import Perfil

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    hashed_password: str
    empresa_id: int = Field(foreign_key="empresa.id")
    is_active: bool = True
    perfil_id: Optional[int] = Field(default=None, foreign_key="perfil.id")

    empresa: Optional["Empresa"] = Relationship(back_populates="usuarios")
    perfil: Optional["Perfil"] = Relationship(back_populates="usuarios")
