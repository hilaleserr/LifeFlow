from datetime import datetime, timedelta
from typing import Union
from jose import JWTError, jwt
from passlib.context import CryptContext

# BU KISIM GİZLİ OLMALI (Gerçek hayatta .env dosyasında saklanır)
SECRET_KEY = "cok_gizli_super_gizli_anahtar_lifeflow"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 1. Şifreyi Hashle (Örn: '123456' -> '$2b$12$KJ/...')
def get_password_hash(password):
    return pwd_context.hash(password)

# 2. Şifreyi Doğrula (Giriş yaparken kullanılır)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 3. Token Oluştur (Kullanıcıya verilen dijital kimlik kartı)
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt