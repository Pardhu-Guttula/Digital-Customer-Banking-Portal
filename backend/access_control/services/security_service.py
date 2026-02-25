# Epic Title: Security Measures for API Integration

from backend.access_control.repositories.security_repository import SecurityRepository
from cryptography.fernet import Fernet
import os
import hashlib
import random
import string
from datetime import datetime, timedelta

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
        otp = ''.join(random.choices(string.digits, k=6))
        expiry_time = datetime.now() + timedelta(minutes=5)
        self.security_repository.store_otp(user_id, otp, expiry_time)
        return otp

    def validate_otp(self, user_id: int, otp: str) -> bool:
        stored_otp, expiry_time = self.security_repository.get_otp(user_id)
        if not stored_otp or datetime.now() > expiry_time:
            return False
        return otp == stored_otp

    def store_user_credentials(self, username: str, password: str):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.security_repository.store_password_hash(username, password_hash)

    def handle_failed_login_attempts(self, username: str):
        self.security_repository.increment_failed_attempts(username)

    def reset_failed_login_attempts(self, username: str):
        self.security_repository.reset_failed_attempts(username)

    def authenticate_user_with_otp(self, username: str, password: str, otp: str) -> bool:
        if not self.validate_user_credentials(username, password):
            self.handle_failed_login_attempts(username)
            return False
        user_id = self.security_repository.get_user_id_by_username(username)
        if not self.validate_otp(user_id, otp):
            self.handle_failed_login_attempts(username)
            return False
        self.reset_failed_login_attempts(username)
        return True
