from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: Optional[int] = None

class ProductCreate(ProductBase):  # ✅ 確保這個類別存在
    pass

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryResponse(CategoryBase):  # 加入這個類別
    id: int

    class Config:
        from_attributes = True

class ProductResponse(ProductBase):
    id: int
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True