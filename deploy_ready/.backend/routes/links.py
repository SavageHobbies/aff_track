from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Link
from schemas import LinkCreate, LinkResponse

router = APIRouter()

@router.post("/", response_model=LinkResponse)
def create_link(link: LinkCreate, db: Session = Depends(get_db)):
    db_link = Link(**link.dict())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

@router.get("/", response_model=List[LinkResponse])
def get_links(db: Session = Depends(get_db)):
    return db.query(Link).all()
