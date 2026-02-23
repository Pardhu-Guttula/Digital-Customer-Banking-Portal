# Epic Title: Address Entry in Checkout Process

from typing import Optional
from pydantic import BaseModel
from backend.checkout.models.address import Address

class Order(BaseModel):
    id: Optional[int]
    user_id: int
    address: Optional[Address]
    total_amount: float

    class Config:
        orm_mode = True