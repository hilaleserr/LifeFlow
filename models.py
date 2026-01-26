from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Role(Base):
    __tablename__ = "roles"
    ID = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    role_id = Column(Integer, ForeignKey("roles.ID"))

class DonorProfile(Base):
    __tablename__ = "donor_profile"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    blood_group = Column(String(5))