from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import get_password_hash, verify_password, create_access_token # Bizim yazdığımız fonksiyonlar
from datetime import timedelta

import models, schemas
from database import SessionLocal, engine

# 1. Veritabanı tablolarını oluştur (Eğer SQL'de oluşturmasaydık bu kod yaratırdı)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LifeFlow Blood Donation API")

# 2. Veritabanı Oturumu (Dependency)
# Her istek geldiğinde veritabanını açar, iş bitince kapatır.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTLER (URL ADRESLERİ) ---

@app.get("/")
def read_root():
    return {"message": "LifeFlow API Çalışıyor! 🩸"}

# 3. Rol Ekleme Endpoint'i (Test için)
@app.post("/roles/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    db_role = models.Role(RoleName=role.RoleName)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

# 4. Kullanıcı Kayıt Endpoint'i (Register)
@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Email kontrolü: Zaten var mı?
    db_user = db.query(models.User).filter(models.User.Email == user.Email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Bu email zaten kayıtlı!")
    
    # Şifreleme (Basitlik için şimdilik 'fake' hash yapıyoruz)
    fake_hashed_password = user.Password + "notreallyhashed"
    
    # Yeni kullanıcıyı hazırla
    new_user = models.User(
        FullName=user.FullName,
        Email=user.Email,
        PasswordHash=fake_hashed_password,
        RoleID=user.RoleID
    )
    
    # Kaydet
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 5. Tüm Kullanıcıları Getir (Admin paneli gibi düşün)
@app.get("/users/", response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# --- LOGIN İŞLEMLERİ ---

# Giriş yapıp Token alma kapısı
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 1. Kullanıcıyı email ile bul (OAuth2 formunda 'username' alanı email olarak kullanılır)
    user = db.query(models.User).filter(models.User.Email == form_data.username).first()
    
    # 2. Kullanıcı yoksa veya şifre yanlışsa hata ver
    if not user or not verify_password(form_data.password, user.PasswordHash):
        raise HTTPException(
            status_code=401,
            detail="E-posta veya şifre hatalı",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Her şey doğruysa Token üret
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.Email, "role": user.RoleID}, # Token içine Rol bilgisini de gömdük!
        expires_delta=access_token_expires
    )
    
    # 4. Token'ı kullanıcıya ver
    return {"access_token": access_token, "token_type": "bearer"}