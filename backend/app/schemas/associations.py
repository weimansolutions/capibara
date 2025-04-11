from pydantic import BaseModel

class CompanyModuleLink(BaseModel):
    company_id: int
    module_id: int

class RolePermissionLink(BaseModel):
    role_id: int
    permission_id: int