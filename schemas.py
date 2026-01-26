from pydantic import BaseModel, EmailStr
from typing import Optional

# Kullanıcı Kayıt Şeması
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role_id: int

# API Cevap Şeması
class UserOut(BaseModel):
    id: int
    email: EmailStr
    role_id: int
    class Config:
        from_attributes = True

# Login Sonrası Verilecek Token Şeması
class Token(BaseModel):
    access_token: str
    token_type: str

# EKSİK OLAN KISIM: Donör Profil Şeması
class DonorProfileCreate(BaseModel):
    blood_group: str

 
class BloodRequestCreate(BaseModel):
    blood_group: str
    urgency: bool # True: Acil, False: Normal
    location: str