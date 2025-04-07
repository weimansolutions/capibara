from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from ..db.database import Base
from app.models.associations import company_modules

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer,primary_key =True) 
    name = Column(String, unique=True)

    users = relationship("User", back_populates="company")
    roles = relationship("Role", back_populates="company")
    modules = relationship("Module", secondary=company_modules, back_populates="companies")


