from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

# 1. SQL Server Ayarları (Senin ekran görüntüne göre ayarladım)
# Server adı: HILAL\SQLEXPRESS
# Veritabanı: BloodDonationDB
SERVER_NAME = 'HILAL\\SQLEXPRESS' 
DATABASE_NAME = 'BloodDonationDB'

# 2. Bağlantı Cümlesi (Connection String)
# Windows Authentication (Trusted_Connection=yes) kullanıyoruz, şifreye gerek yok.
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER_NAME};"
    f"DATABASE={DATABASE_NAME};"
    f"Trusted_Connection=yes;"
)

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

# 3. Motoru (Engine) Başlat
engine = create_engine(DATABASE_URL)

# 4. Oturum (Session) Oluşturucu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base Sınıfı (Modellerimiz bundan türeyecek)
Base = declarative_base()

# Bağlantıyı test etmek için küçük bir fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()