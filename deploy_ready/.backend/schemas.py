from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LinkBase(BaseModel):
    url: str
    description: Optional[str] = None

class LinkCreate(LinkBase):
    pass

class LinkResponse(LinkBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class DataBase(BaseModel):
    key: str
    value: str

class DataCreate(DataBase):
    pass

class DataResponse(DataBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True
