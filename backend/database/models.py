# Epic Title: Integrate PostgreSQL Database for Data Management in the Admin Dashboard

from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.config import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)

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