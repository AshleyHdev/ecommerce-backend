from sqlalchemy import Column, Integer, String, Float, ForeignKey  # 確保 Float 在這裡
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()  # 確保有這行

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
    price = Column(Float)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))

    # 關聯類別
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price}, stock={self.stock})>"

# 將 __all__ 放到最外層
__all__ = ["Base", "Category", "Product"]