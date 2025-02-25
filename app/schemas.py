from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

# ✅ 商品基礎模型
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: Optional[int] = None

# ✅ 用於創建商品的結構
class ProductCreate(ProductBase):
    pass

# ✅ 用於回應的商品結構
class Product(ProductBase):
    id: int  # ✅ 確保回應有 id
    
    class Config:
        from_attributes = True  # ✅ 確保與 ORM 兼容

# ✅ 分類基礎模型
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

# ✅ 用於創建分類的結構
class CategoryCreate(CategoryBase):
    pass

# ✅ 用於回應的分類結構
class Category(CategoryBase):
    id: int  # ✅ 確保回應有 id
    
    class Config:
        from_attributes = True  # ✅ 確保與 ORM 兼容