from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from ..db.database import Base
from .associations import role_permissions

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))

    # Relaciones
    company = relationship("Company", back_populates="roles")         # N:1 con Company
    users = relationship("User", back_populates="role")               # 1:N con User
    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")  # N:M con Permission
