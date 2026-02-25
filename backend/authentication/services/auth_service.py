# Epic Title: Develop Secure Authentication Mechanisms Using FastAPI

from backend.authentication.repositories.auth_repository import AuthRepository
from backend.authentication.models.user import User
from backend.authentication.models.token import Token
from backend.authentication.models.otp import OTP
import logging
import bcrypt
import jwt
from datetime import datetime, timedelta

class AuthService:
    def __init__(self):
        self.repository = AuthRepository()
        self.secret_key = "your-secret-key"

    def login(self, user: User) -> str:
        stored_user = self.repository.get_user_by_email(user.email)
        if not stored_user:
            raise ValueError("User not found")

        if not bcrypt.checkpw(user.password.encode(), stored_user.password_hash.encode()):
            raise ValueError("Invalid credentials")

        # Generate token
        expiration = datetime.utcnow() + timedelta(hours=1)
        token = jwt.encode({"email": stored_user.email, "exp": expiration}, self.secret_key, algorithm="HS256")
        return token

    def verify_otp(self, email: str, otp: str):
        stored_otp = self.repository.get_otp_by_email(email)
        if stored_otp and stored_otp.otp == otp:
            self.repository.invalidate_otp(email)
            return
        raise ValueError("Invalid OTP")

    def store_user_credentials(self, user: User):
        hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
        self.repository.create_user(user.email, hashed_password)