# Epic Title: Secure Login System with MFA

from sqlalchemy import Column, Integer, String
from backend.database.config import Base
from cryptography.fernet import Fernet
import os

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def set_password(self, plaintext_password: str):
        key = os.getenv('ENCRYPTION_KEY').encode()
        cipher_suite = Fernet(key)
        self.password = cipher_suite.encrypt(plaintext_password.encode()).decode()

    def check_password(self, plaintext_password: str) -> bool:
        key = os.getenv('ENCRYPTION_KEY').encode()
        cipher_suite = Fernet(key)
        decrypted_password = cipher_suite.decrypt(self.password.encode()).decode()
        return decrypted_password == plaintext_password