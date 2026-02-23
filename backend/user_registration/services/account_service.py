# Epic Title: User Registration Form

from sqlalchemy.orm import Session
from backend.user_registration.repositories.account_repository import AccountRepository

class AccountService:
    PASSWORD_MIN_LENGTH_ERROR = "Password must be at least 8 characters long."
    
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def validate_password(self, password: str) -> bool:
        return len(password) >= 8

    def create_account(self, db: Session, name: str, email: str, password: str) -> dict:
        if not self.validate_password(password):
            return {"success": False, "error": self.PASSWORD_MIN_LENGTH_ERROR}
        existing_account = self.account_repository.get_account_by_email(email)
        if existing_account:
            return {"success": False, "error": "Email already registered."}
        account = self.account_repository.create_account(name, email, password)
        return {"success": True, "account": account}