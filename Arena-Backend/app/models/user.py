from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # hashé idéalement
    number = Column(String(50), nullable=True)  # ton champ number
    created_at = Column(DateTime, default=datetime.utcnow)