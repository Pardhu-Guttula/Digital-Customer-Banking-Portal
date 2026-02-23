# Epic Title: Secure Login System with MFA

from sqlalchemy.orm import Session
from backend.authentication.models.account import Account
from typing import Optional

class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_account_by_email(self, email: str) -> Optional[Account]:
        return self.db.query(Account).filter(Account.email == email).first()

    def create_account(self, name: str, email: str, password: str) -> Account:
        account = Account(name=name, email=email)
        account.set_password(password)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def validate_login(self, email: str, password: str) -> Optional[Account]:
        account = self.get_account_by_email(email)
        if account and account.check_password(password):
            return account
        return None