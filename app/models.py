from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime

# 定義 Base 類別
class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)

    # 關聯商品
    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    created_at = Column(DateTime, default=datetime.utcnow)  # 自動新增的時間戳
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # 自動更新的時間戳

    # 關聯類別
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return (
            f"<Product(id={self.id}, name={self.name}, price={self.price}, "
            f"stock={self.stock}, created_at={self.created_at})>"
        )

# 將 __all__ 放到最外層
__all__ = ["Base", "Category", "Product"]