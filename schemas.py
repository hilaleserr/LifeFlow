from pydantic import BaseModel
from typing import Optional

# 1. Rol Şemaları (Veri alıp verirken kullanılacak kalıplar)
class RoleBase(BaseModel):
    RoleName: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    RoleID: int
    class Config:
        from_attributes = True # ORM modunu açar (SQLAlchemy ile uyum için)

# 2. Kullanıcı Oluşturma Şeması (Kayıt olurken istenecek bilgiler)
class UserCreate(BaseModel):
    FullName: str
    Email: str
    Password: str # Buraya dikkat: Kullanıcıdan 'Password' alırız...
    RoleID: int = 2 # Varsayılan olarak 2 (Donor) olsun

# 3. Kullanıcı Okuma Şeması (API cevap dönerken gösterilecek bilgiler)
class UserOut(BaseModel):
    UserID: int
    FullName: str
    Email: str
    # DİKKAT: Password'ü burada döndürmüyoruz! Güvenlik kuralı.
    
    class Config:
        from_attributes = True