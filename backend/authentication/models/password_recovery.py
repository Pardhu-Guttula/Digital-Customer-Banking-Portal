# Epic Title: Password Recovery

from pydantic import BaseModel, EmailStr

class PasswordRecovery(BaseModel):
    email: EmailStr