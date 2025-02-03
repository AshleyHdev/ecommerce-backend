from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import products, categories  # 匯入 routes

# 自動建立資料表
Base.metadata.create_all(bind=engine)

# 建立 FastAPI 應用
app = FastAPI()

# 註冊路由
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])

@app.get("/")
def read_root():
    return {"message": "歡迎使用電子商務 API！"}