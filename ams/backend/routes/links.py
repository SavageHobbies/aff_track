from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Link
from ..schemas import LinkCreate, LinkUpdate, LinkResponse

router = APIRouter()

@router.delete("/links/{link_id}")
async def delete_link(link_id: int, db: Session = Depends(get_db)):
    """Delete a single link"""
    link = db.query(Link).filter(Link.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    db.delete(link)
    db.commit()
    return {"message": "Link deleted successfully"}

@router.delete("/links/bulk")
async def bulk_delete_links(link_ids: List[int], db: Session = Depends(get_db)):
    """Delete multiple links at once"""
    # Verify all links exist
    links = db.query(Link).filter(Link.id.in_(link_ids)).all()
    if len(links) != len(link_ids):
        raise HTTPException(status_code=404, detail="Some links were not found")
    
    # Delete all links
    for link in links:
        db.delete(link)
    db.commit()
    
    return {"message": f"Successfully deleted {len(links)} links"}
