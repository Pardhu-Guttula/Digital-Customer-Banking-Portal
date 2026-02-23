# Epic Title: Store Order and Payment Information in PostgreSQL

from typing import Optional
from pydantic import BaseModel, constr

class Payment(BaseModel):
    id: Optional[int]
    user_id: int
    order_id: int
    card_number: constr(min_length=12, max_length=19)
    card_expiry: constr(min_length=5, max_length=5)
    card_cvv: constr(min_length=3, max_length=4)
    amount: float

    class Config:
        orm_mode = True