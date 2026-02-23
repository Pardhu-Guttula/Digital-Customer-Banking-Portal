# Epic Title: Update Product Quantity in Shopping Cart

from typing import Optional, List
from pydantic import BaseModel, condecimal

class CartItem(BaseModel):
    product_id: int
    quantity: int

class Cart(BaseModel):
    id: Optional[int]
    user_id: int
    items: List[CartItem] = []

    class Config:
        orm_mode = True