from sqlalchemy.orm import Session
from app import models, schemas
from app.schemas import ProductCreate

def create_product(db: Session, product: schemas.ProductCreate):  # ✅ 確保這裡沒拼錯
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 取得所有商品
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

# 取得單個商品
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# 更新商品
def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

# 刪除商品
def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product