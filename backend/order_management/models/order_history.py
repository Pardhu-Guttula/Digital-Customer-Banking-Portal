# Epic Title: Allow Users to View Order History

from typing import List
from pydantic import BaseModel
from backend.order_management.models.order import Order

class OrderHistory(BaseModel):
    orders: List[Order]

    class Config:
        orm_mode = True