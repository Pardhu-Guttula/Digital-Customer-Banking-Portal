# Epic Title: Payment Processing During Checkout

from typing import Optional
from pydantic import BaseModel
from backend.checkout.models.payment import Payment

class Order(BaseModel):
    id: Optional[int]
    user_id: int
    address_id: Optional[int]
    payment_id: Optional[int]
    total_amount: float

    class Config:
        orm_mode = True