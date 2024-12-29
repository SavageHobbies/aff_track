from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Data
from schemas import DataCreate, DataResponse

router = APIRouter()

@router.post("/", response_model=DataResponse)
def create_data(data: DataCreate, db: Session = Depends(get_db)):
    db_data = Data(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.get("/")
def get_data(db: Session = Depends(get_db)):
    return db.query(Data).all()
