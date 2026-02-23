# Epic Title: Track User Orders

from typing import Optional, List
from pydantic import BaseModel

class OrderStatus(BaseModel):
    id: Optional[int]
    status: str

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float

class Order(BaseModel):
    id: Optional[int]
    user_id: int
    address_id: Optional[int]
    items: List[OrderItem]
    total_amount: float
    status: OrderStatus

    class Config:
        orm_mode = True