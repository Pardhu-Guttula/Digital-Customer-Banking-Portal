# Epic Title: User Registration

from typing import Optional
from pydantic import BaseModel, EmailStr, constr

class User(BaseModel):
    id: Optional[int]
    email: EmailStr
    password: constr(min_length=8)

    class Config:
        orm_mode = True