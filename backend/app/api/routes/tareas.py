from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.models import Tarea
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class TareaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    usuario_id: int

class TareaOut(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    estado: str
    usuario_id: int

    class Config:
        orm_mode = True

@router.post("/crear_task", response_model=TareaOut)
def crear_tarea(data: TareaCreate, session: Session = Depends(get_session)):
    tarea = Tarea(**data.dict())
    session.add(tarea)
    session.commit()
    session.refresh(tarea)
    return tarea

@router.get("/usuario/{usuario_id}", response_model=List[TareaOut])
def tareas_por_usuario(usuario_id: int, session: Session = Depends(get_session)):
    tareas = session.exec(select(Tarea).where(Tarea.usuario_id == usuario_id)).all()
    return tareas

@router.put("/{tarea_id}/completar", response_model=TareaOut)
def completar_tarea(tarea_id: int, session: Session = Depends(get_session)):
    tarea = session.get(Tarea, tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.estado = "completada"
    session.add(tarea)
    session.commit()
    session.refresh(tarea)
    return tarea
