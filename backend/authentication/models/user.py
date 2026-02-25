# Epic Title: Develop Secure Authentication Mechanisms Using FastAPI

from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str
    password_hash: str = None