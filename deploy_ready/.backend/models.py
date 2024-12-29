from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from database import Base

class Link(Base):
    __tablename__ = "links"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    name = Column(String)
    clicks = Column(Integer, default=0)
    revenue = Column(Float, default=0.0)
