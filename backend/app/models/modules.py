from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from ..db.database import Base
from app.models.associations import company_modules

class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Relaciones
    permissions = relationship("Permission", back_populates="module")         # 1:N con Permission
    companies = relationship("Company", secondary=company_modules, back_populates="modules")  # N:M con Company
