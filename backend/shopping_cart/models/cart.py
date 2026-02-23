# Epic Title: Persist Shopping Cart Data in PostgreSQL

from typing import Optional, List
from pydantic import BaseModel

class CartItem(BaseModel):
    id: Optional[int]
    product_id: int
    quantity: int

class Cart(BaseModel):
    id: Optional[int]
    user_id: int
    items: List[CartItem] = []

    class Config:
        orm_mode = True