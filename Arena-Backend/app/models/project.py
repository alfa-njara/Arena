from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .base import Base
from datetime import datetime


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    stack = Column(Text)
    contact = Column(String(255))
    url = Column(String(255))
    icon = Column(String(100))
    likes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)