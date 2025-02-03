import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 讀取 DATABASE_URL（避免寫死）
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("❌ DATABASE_URL 未設定，請確認環境變數已正確設定！")

# 修正 SQLAlchemy 無法識別 "postgres://" 的問題
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Heroku 的 PostgreSQL 需要 SSL 連線
engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})

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