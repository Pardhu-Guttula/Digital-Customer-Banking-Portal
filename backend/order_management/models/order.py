# Epic Title: Store Order and Payment Information in PostgreSQL

from typing import Optional
from pydantic import BaseModel
from backend.checkout.models.payment import Payment
from backend.checkout.models.address import Address

class Order(BaseModel):
    id: Optional[int]
    user_id: int
    address_id: Optional[int]
    payment_id: Optional[int]
    total_amount: float

    class Config:
        orm_mode = True