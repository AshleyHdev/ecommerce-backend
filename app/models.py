from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, DeclarativeBase

# ✅ 使用 SQLAlchemy 2.0 建議的方式建立 Base
class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)

    # ✅ 關聯商品
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Category(id={self.id!r}, name={self.name!r})>"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # ✅ 加入時間戳記
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # ✅ 關聯類別
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id!r}, name={self.name!r}, price={self.price!r}, stock={self.stock!r})>"

# ✅ 讓其他模組可以 import 這些類別
__all__ = ["Base", "Category", "Product"]