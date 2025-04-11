from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models

def assign_module_to_company(db: Session, company_id: int, module_id: int):
    company = db.query(models.Company).filter(models.Company.id == company_id).first()
    module = db.query(models.Module).filter(models.Module.id == module_id).first()
    
    if not company or not module:
        raise HTTPException(status_code=404, detail="Company or Module not found")

    if module not in company.modules:
        company.modules.append(module)
        db.commit()
    
    return {"message": "Module successfully assigned to company"}

def assign_permission_to_role(db: Session, permission_id: int, role_id: int):
    permission = db.query(models.Permission).filter(models.Permission.id == permission_id).first()
    role = db.query(models.Role).filter(models.Role.id == role_id).first()
    
    if not permission or not role:
        raise HTTPException(status_code=404, detail="Permission or Role not found")

    if permission not in role.permissions:
        role.permissions.append(permission)
        db.commit()
    
    return {"message": "Permission successfully assigned to Role"}