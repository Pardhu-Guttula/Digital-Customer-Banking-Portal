# Epic Title: Security Measures for API Integration

from backend.access_control.repositories.security_repository import SecurityRepository
from cryptography.fernet import Fernet
import os
import hashlib

class SecurityService:
    def __init__(self, db):
        self.security_repository = SecurityRepository(db)
        self.cipher_suite = Fernet(os.environ.get('ENCRYPTION_KEY').encode())

    def validate_token(self, token: str):
        if not token:
            raise ValueError("Missing token")
        if not self.security_repository.verify_token(token):
            raise ValueError("Invalid or expired token")

    def encrypt_sensitive_data(self, data: dict):
        if 'banking_data' in data:
            data['banking_data'] = self.cipher_suite.encrypt(data['banking_data'].encode()).decode()
        return data

    def validate_user_credentials(self, username: str, password: str) -> bool:
        stored_password_hash = self.security_repository.get_password_hash(username)
        if not stored_password_hash:
            return False
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash == stored_password_hash

    def generate_otp(self, user_id: int) -> str:
        otp = self.security_repository.create_otp(user_id)
        return otp

    def validate_otp(self, user_id: int, otp: str) -> bool:
        stored_otp = self.security_repository.get_otp(user_id)
        if not stored_otp:
            return False
        return otp == stored_otp