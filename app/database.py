import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 讀取環境變數
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL 未設定，請確認環境變數已正確設定！")

# Heroku 的 PostgreSQL 需要 SSL 連線，其他類型資料庫不需要
connect_args = {}
if DATABASE_URL.startswith("postgres://"):
    connect_args = {"sslmode": "require"}

# 創建 SQLAlchemy 引擎
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# 建立 Session 和 Base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 建立一個函式來獲取資料庫連線
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()