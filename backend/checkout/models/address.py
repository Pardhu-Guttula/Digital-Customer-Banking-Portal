# Epic Title: Address Entry in Checkout Process

from typing import Optional
from pydantic import BaseModel, constr

class Address(BaseModel):
    id: Optional[int]
    user_id: int
    street: constr(min_length=5, max_length=100)
    city: constr(min_length=2, max_length=50)
    state: constr(min_length=2, max_length=50)
    postal_code: constr(min_length=5, max_length=10)
    country: constr(min_length=2, max_length=50)

    class Config:
        orm_mode = True