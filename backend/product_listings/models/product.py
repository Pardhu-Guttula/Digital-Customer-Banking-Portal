# Epic Title: Develop Product Listing Page

from typing import Optional
from pydantic import BaseModel, condecimal

class Product(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: condecimal(max_digits=10, decimal_places=2)
    stock_quantity: int

    class Config:
        orm_mode = True