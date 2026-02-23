# Epic Title: Multi-Factor Authentication Setup

from sqlalchemy.orm import Session
from backend.authentication.repositories.mfa_repository import MFARepository
import random
import string

class MFAService:
    def __init__(self, mfa_repository: MFARepository):
        self.mfa_repository = mfa_repository

    def generate_token(self) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def setup_mfa(self, db: Session, account_id: int, mfa_method: str) -> dict:
        mfa_setup = self.mfa_repository.create_mfa_setup(account_id, mfa_method)
        return {"success": True, "mfa_setup": mfa_setup}

    def activate_mfa(self, db: Session, account_id: int, mfa_method: str) -> dict:
        self.mfa_repository.activate_mfa_setup(account_id, mfa_method)
        token = self.generate_token()
        mfa_token = self.mfa_repository.create_token(account_id, token)
        return {"success": True, "token": mfa_token.token}

    def validate_mfa_token(self, db: Session, account_id: int, token: str) -> dict:
        is_valid = self.mfa_repository.validate_token(account_id, token)
        return {"success": is_valid}