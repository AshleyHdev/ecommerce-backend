from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import products  # 確保有 import products

app = FastAPI()

# 確保有這行
app.include_router(products.router, prefix="/products", tags=["Products"])

@app.get("/")
def read_root():
    return {"message": "歡迎使用電子商務 API！"}