# Epic Title: Integrate PostgreSQL for Storing User Credentials

from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str