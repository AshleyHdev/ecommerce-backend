from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import products

app = FastAPI()

# 自動建立資料表
Base.metadata.create_all(bind=engine)

# ✅ 註冊路由
app.include_router(products.router, prefix="/products", tags=["Products"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API!"}