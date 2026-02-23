from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .base import Base
from datetime import datetime


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    date = Column(DateTime)
    location = Column(String(255))
    image = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)