from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.database import get_session
from app.models.companies import Company
from app.schemas.companies import CompanyCreate
from app.api.deps.auth import get_current_active_user,require_superadmin
from app.crud.associations import assign_module_to_company
from app.schemas.associations import CompanyModuleLink
from app.models.users import User

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("/assign-module", dependencies=[Depends(require_superadmin)])
def assign_module(data: CompanyModuleLink, db: Session = Depends(get_session)):
    return assign_module_to_company(db, data.company_id, data.module_id)

@router.post("/inicial", status_code=status.HTTP_201_CREATED)
def create_initial_company(
    company_in: CompanyCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(require_superadmin)
    ):

    company = Company(
        name=company_in.name
    )
    session.add(company)
    session.commit()
    session.refresh(company)
    return {"message": "Empresa creada correctamente", "id": company.id}

@router.get("/listar", status_code=status.HTTP_201_CREATED)
def list_companies(
    session: Session = Depends(get_session),
    current_user: User = Depends(require_superadmin)
    ):

    return session.query(Company).all()