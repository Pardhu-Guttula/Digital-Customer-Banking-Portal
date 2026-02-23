# Epic Title: User Registration Backend Logic

from sqlalchemy.orm import Session
from backend.user_registration.repositories.account_repository import AccountRepository

class AccountService:
    PASSWORD_MIN_LENGTH_ERROR = "Password must be at least 8 characters long."
    EMAIL_DUPLICATE_ERROR = "Email already registered."
    GENERAL_VALIDATION_ERROR = "Invalid registration data."

    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def validate_password(self, password: str) -> bool:
        return len(password) >= 8

    def validate_registration_data(self, name: str, email: str, password: str) -> Optional[str]:
        if not name or not email or not password:
            return self.GENERAL_VALIDATION_ERROR
        if not self.validate_password(password):
            return self.PASSWORD_MIN_LENGTH_ERROR
        existing_account = self.account_repository.get_account_by_email(email)
        if existing_account:
            return self.EMAIL_DUPLICATE_ERROR
        return None

    def create_account(self, db: Session, name: str, email: str, password: str) -> dict:
        validation_error = self.validate_registration_data(name, email, password)
        if validation_error:
            return {"success": False, "error": validation_error}
        account = self.account_repository.create_account(name, email, password)
        return {"success": True, "account": account}