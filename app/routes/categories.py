from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter()

# ✅ 新增分類（POST /categories）
@router.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

# ✅ 取得所有分類（GET /categories）
@router.get("/categories", response_model=list[schemas.Category])
def get_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

# ✅ 取得特定分類（GET /categories/{category_id}）
@router.get("/categories/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category