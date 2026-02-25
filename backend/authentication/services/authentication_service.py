# Epic Title: User Authentication and Session Management for Secure Login

from typing import Optional
import jwt
from backend.authentication.models.user import UserRepository, User
import logging

class AuthenticationService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.secret_key = 'your_secret_key'

    def authenticate(self, email: str, password: str) -> Optional[User]:
        user = self.user_repository.find_by_email(email)
        if user and user.verify_password(password):
            return user
        return None

    def generate_session_token(self, user: User) -> str:
        payload = {'user_id': user.id}
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token