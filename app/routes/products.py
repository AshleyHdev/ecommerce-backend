from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(
    prefix="/products",  # 路徑前綴
    tags=["Products"]  # 標籤名稱
)

# 取得資料庫 Session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 新增商品
@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        products = crud.get_products(db, skip=skip, limit=limit)
        print("🚀 查詢結果:", products)  # 檢查是否正確取出資料
        return products
    except Exception as e:
        print("❌ 發生錯誤:", e)  # 這行會顯示完整的錯誤資訊
        raise HTTPException(status_code=500, detail=str(e))

# 取得單個商品
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# 更新商品
@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

# 刪除商品
@router.delete("/{product_id}", response_model=schemas.ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product