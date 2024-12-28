from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class LinkBase(BaseModel):
    url: str
    name: str
    status: Optional[str] = "active"
    category: Optional[str] = None

class LinkCreate(LinkBase):
    pass

class LinkUpdate(LinkBase):
    url: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    category: Optional[str] = None

class LinkResponse(LinkBase):
    id: int
    clicks: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
