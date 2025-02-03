from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(
    prefix="/products",  # ✅ 確保這裡沒有錯誤
    tags=["Products"]  # ✅ FastAPI 內建的 API 標籤
)

# 取得資料庫 Session（依賴注入）
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ 新增商品
@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

# ✅ 取得所有商品
@router.get("/", response_model=list[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        products = crud.get_products(db, skip=skip, limit=limit)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ 取得單個商品
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# ✅ 更新商品
@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

# ✅ 刪除商品
@router.delete("/{product_id}", response_model=schemas.ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product