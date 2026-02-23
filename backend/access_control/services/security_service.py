# Epic Title: Security Measures for API Integration

from backend.access_control.repositories.security_repository import SecurityRepository
from cryptography.fernet import Fernet

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