# models/associations.py
from sqlalchemy import Table, Column, ForeignKey
from ..db.database import Base

role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", ForeignKey("permissions.id"), primary_key=True)
)

company_modules = Table(
    "company_modules",
    Base.metadata,
    Column("company_id", ForeignKey("companies.id"), primary_key=True),
    Column("module_id", ForeignKey("modules.id"), primary_key=True)
)
