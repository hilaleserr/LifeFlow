from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from datetime import timedelta

# Kendi modüllerimizi dahil ediyoruz
import models, schemas, auth
from database import SessionLocal, engine

# 1. Veritabanı tablolarını oluştur (Eğer yoksa)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LifeFlow Blood Donation API")

# 2. CORS Ayarları (Flutter'ın bağlanabilmesi için ÇOK ÖNEMLİ)
# Bu ayar sayesinde emülatörden veya telefondan gelen isteklere "Red" cevabı verilmez.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Güvenlik için ileride buraya sadece kendi domainini yazarsın
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE hepsine izin ver
    allow_headers=["*"],
)

# 3. Veritabanı Oturumu (Dependency)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================================================
# GÜVENLİK VE GİRİŞ İŞLEMLERİ (AUTH)
# =========================================================

@app.post("/token", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Kullanıcı Girişi (Login)
    - Kullanıcı Email ve Şifresini gönderir.
    - Doğruysa, süreli bir 'Access Token' (Anahtar) alır.
    """
    # 1. Kullanıcıyı Email ile bul
    # (OAuth2 formunda 'username' alanı bizim sistemde 'Email'e karşılık gelir)
    user = db.query(models.User).filter(models.User.Email == form_data.username).first()
    
    # 2. Kullanıcı yoksa VEYA şifre yanlışsa hata fırlat
    if not user or not auth.verify_password(form_data.password, user.PasswordHash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Hatalı E-posta veya Şifre",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Her şey doğruysa Token üret
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.Email, "role": user.RoleID}, # Token içine Rol bilgisini gömdük
        expires_delta=access_token_expires
    )
    
    # 4. Token'ı dön
    return {"access_token": access_token, "token_type": "bearer"}


# =========================================================
# KULLANICI İŞLEMLERİ (USER)
# =========================================================

@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Yeni Kullanıcı Kaydı (Register)
    - Şifreyi veritabanına kaydetmeden önce HASH'ler (şifreler).
    """
    # Email kontrolü: Zaten var mı?
    db_user = db.query(models.User).filter(models.User.Email == user.Email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Bu e-posta adresi zaten kayıtlı!")
    
    # Şifreyi Hashle (Güvenli hale getir)
    hashed_password = auth.get_password_hash(user.Password)
    
    # Yeni kullanıcı nesnesini oluştur
    new_user = models.User(
        FullName=user.FullName,
        Email=user.Email,
        PasswordHash=hashed_password, # Hashlenmiş şifreyi kaydediyoruz
        RoleID=user.RoleID
    )
    
    # Kaydet
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/", response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Tüm Kullanıcıları Listele (Admin Paneli İçin)
    """
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# =========================================================
# YARDIMCI ENDPOINTLER
# =========================================================

@app.post("/roles/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    """
    Rol Ekleme (Sadece ilk kurulumda lazım olur)
    """
    db_role = models.Role(RoleName=role.RoleName)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@app.get("/")
def read_root():
    return {"message": "LifeFlow API Çalışıyor! 🩸 (v1.0)"}