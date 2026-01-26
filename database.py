from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

# MSSQL Bağlantı Bilgileri
params = urllib.parse.quote_plus(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=HILAL\SQLEXPRESS;'  # Senin sunucu adın
    r'DATABASE=BloodDonationDB;' # Veritabanı adın
    r'Trusted_Connection=yes;'   # Windows kimlik doğrulaması
)

SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()