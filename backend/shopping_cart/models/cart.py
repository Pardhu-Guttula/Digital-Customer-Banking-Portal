# Epic Title: Remove Product from Shopping Cart

from typing import Optional, List
from pydantic import BaseModel

class CartItem(BaseModel):
    product_id: int
    quantity: int

class Cart(BaseModel):
    id: Optional[int]
    user_id: int
    items: List[CartItem] = []

    class Config:
        orm_mode = True