from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

# Product 基礎模型
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: Optional[int] = None

# 用於創建商品的結構
class ProductCreate(ProductBase):
    pass

# Category 基礎模型
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

# 用於創建分類的結構
class CategoryCreate(CategoryBase):  # ✅ 新增這個類別
    pass

# 回應用的 Category 結構
class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True  # 確保與 ORM 兼容

# 回應用的 Product 結構
class ProductResponse(ProductBase):
    id: int
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True  # 確保與 ORM 兼容