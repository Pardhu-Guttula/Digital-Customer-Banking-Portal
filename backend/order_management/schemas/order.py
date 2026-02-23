# Epic Title: Integrate with PostgreSQL for Data Storage

from typing import Optional, List
from pydantic import BaseModel

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(OrderItemBase):
    id: int

class OrderItemOut(OrderItemBase):
    id: int

class OrderStatusBase(BaseModel):
    status: str

class OrderStatusOut(OrderStatusBase):
    id: int

class OrderBase(BaseModel):
    user_id: int
    address_id: int
    total_amount: float
    status_id: int
    date: str

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderUpdate(OrderBase):
    items: List[OrderItemUpdate]

class OrderOut(OrderBase):
    id: int
    items: List[OrderItemOut]
    status: OrderStatusOut

    class Config:
        orm_mode = True