from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from ..db.database import Base
from .associations import role_permissions

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    name = Column(String)  # Ej: "create_item", "edit_item"
    description = Column(String,nullable = True)
    module_id = Column(Integer, ForeignKey("modules.id"))

    # Relaciones
    module = relationship("Module", back_populates="permissions")     # N:1 con Module
    roles = relationship("Role", secondary=role_permissions, back_populates="permissions")  # N:M con Role

    __table_args__ = (UniqueConstraint('name', 'module_id', name='uq_permission_module'),)
