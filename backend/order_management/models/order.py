# Epic Title: Order Confirmation Display After Successful Purchase

from typing import Optional, List
from pydantic import BaseModel
from backend.checkout.models.address import Address

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

    class Config:
        orm_mode = True