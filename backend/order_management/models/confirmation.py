# Epic Title: Order Confirmation Display After Successful Purchase

from typing import List, Dict
from pydantic import BaseModel

class Confirmation(BaseModel):
    order_number: int
    items: List[Dict[str, float]]
    total_amount: float
    delivery_information: str

    class Config:
        orm_mode = True