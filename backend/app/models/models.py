# app/models/models.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Empresa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    hashed_password: str
    empresa_id: int = Field(foreign_key="empresa.id")
    is_active: bool = True
    perfil_id: Optional[int] = Field(default=None, foreign_key="perfil.id")

class Perfil(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    empresa_id: int = Field(foreign_key="empresa.id")

class Rol(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    empresa_id: int = Field(foreign_key="empresa.id")

class Permiso(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: Optional[str] = None

class Tarea(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    descripcion: Optional[str] = None
    estado: str = "pendiente"
    usuario_id: int = Field(foreign_key="usuario.id")