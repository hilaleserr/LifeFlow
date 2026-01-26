from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import List

import models, schemas
from database import SessionLocal, engine

# 1. Güvenlik Ayarları
SECRET_KEY = "lifeflow_cok_gizli_anahtar"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# 2. Veritabanı Başlatma
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LifeFlow Blood Donation API")

# 3. Yardımcı Fonksiyonlar (Dependencies)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Kimlik bilgileri doğrulanamadı",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user

# ---------------------------------------------------------
# 4. API ENDPOINT'LERİ
# ---------------------------------------------------------

@app.get("/")
def read_root():
    return {"message": "LifeFlow API Çalışıyor!"}

# --- KAYIT OLMA ---
@app.post("/register", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Bu email zaten kayıtlı.")
    
    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(email=user.email, password=hashed_password, role_id=user.role_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# --- GİRİŞ YAPMA (TOKEN ALMA) ---
@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Hatalı email veya şifre")

    access_token = jwt.encode({"sub": user.email}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}

# --- DONÖR PROFİLİ OLUŞTURMA ---
@app.post("/donor-profile")
def create_donor_profile(
    profile: schemas.DonorProfileCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    existing_profile = db.query(models.DonorProfile).filter(models.DonorProfile.user_id == current_user.id).first()
    if existing_profile:
        raise HTTPException(status_code=400, detail="Donör profiliniz zaten mevcut.")
    
    new_profile = models.DonorProfile(user_id=current_user.id, blood_group=profile.blood_group)
    db.add(new_profile)
    db.commit()
    return {"message": "Donör profili başarıyla oluşturuldu", "blood_group": profile.blood_group}