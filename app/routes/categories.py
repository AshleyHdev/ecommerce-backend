from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, schemas, crud

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@router.get("/", response_model=list[schemas.CategoryResponse])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)