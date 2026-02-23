# Epic Title: Track User Orders

from typing import Optional
from pydantic import BaseModel

class OrderStatus(BaseModel):
    id: Optional[int]
    status: str

    class Config:
        orm_mode = True