# Epic Title: Integrate with PostgreSQL for Data Storage

from typing import Optional, List
from sqlalchemy import Column, Integer, Float, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import relationship
from backend.database.config import Base

class OrderStatus(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    address_id = Column(Integer, nullable=False)
    total_amount = Column(Float, nullable=False)
    status_id = Column(Integer, ForeignKey("statuses.id"), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    
    items = relationship("OrderItem", back_populates="order")
    status = relationship("OrderStatus")