from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# 建立資料庫引擎
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 建立一個函式來獲取資料庫連線
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()