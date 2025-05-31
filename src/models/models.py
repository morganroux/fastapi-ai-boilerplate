from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

Base = declarative_base()

# SQLAlchemy Models
class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    orders = relationship("OrderModel", back_populates="user")

class OrderModel(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("UserModel", back_populates="orders")

# Pydantic schemas
class UserCreate(BaseModel):
    username: str
    email: str

class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    user_id: int
    total_amount: float

class Order(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True