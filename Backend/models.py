from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

# 1. Roller Modeli (dbo.roles)
class Role(Base):
    __tablename__ = "roles"

    RoleID = Column(Integer, primary_key=True, index=True)
    RoleName = Column(String(50), nullable=False)

    # İlişki: Bir rolün birden çok kullanıcısı olabilir
    users = relationship("User", back_populates="role")

# 2. Kullanıcılar Modeli (dbo.users)
class User(Base):
    __tablename__ = "users"

    UserID = Column(Integer, primary_key=True, index=True)
    FullName = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    PasswordHash = Column(String(255), nullable=False)
    RoleID = Column(Integer, ForeignKey("roles.RoleID"), nullable=False)
    CreatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # İlişkiler
    role = relationship("Role", back_populates="users")
    profile = relationship("DonorProfile", back_populates="user", uselist=False) # Bire-bir ilişki
    requests = relationship("BloodRequest", back_populates="requester")

# 3. Bağışçı Profili Modeli (dbo.donor_profile)
class DonorProfile(Base):
    __tablename__ = "donor_profile"

    ProfileID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("users.UserID"), unique=True, nullable=False)
    BloodGroup = Column(String(5), nullable=False)
    Phone = Column(String(15))
    Latitude = Column(Float)
    Longitude = Column(Float)
    LastDonationDate = Column(Date)

    # İlişki: Bu profil kime ait?
    user = relationship("User", back_populates="profile")

# 4. Kan Talepleri Modeli (dbo.blood_requests)
class BloodRequest(Base):
    __tablename__ = "blood_requests"

    RequestID = Column(Integer, primary_key=True, index=True)
    RequesterID = Column(Integer, ForeignKey("users.UserID"), nullable=False)
    BloodGroup = Column(String(5), nullable=False)
    UrgencyLevel = Column(Integer, default=1)
    Latitude = Column(Float)
    Longitude = Column(Float)
    Status = Column(String(20), default="Active")
    IsActive = Column(Boolean, default=True)
    CreatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # İlişki: Talebi kim oluşturdu?
    requester = relationship("User", back_populates="requests")