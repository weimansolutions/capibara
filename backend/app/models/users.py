from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from ..db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    username = Column(String,unique = True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String,unique = True)
    phone = Column(String(20), unique = True,nullable = True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default = True)
    is_superadmin = Column(Boolean, default = False)

    company_id = Column(Integer,ForeignKey("companies.id"), nullable = True)
    role_id = Column(Integer,ForeignKey("roles.id"),nullable = True)

    company = relationship("Company", back_populates ="users")
    role = relationship("Role", back_populates="users")

