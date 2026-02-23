# Epic Title: User Registration Backend Logic

from sqlalchemy.orm import Session
from backend.user_registration.models.account import Account
from typing import Optional

class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_account_by_email(self, email: str) -> Optional[Account]:
        return self.db.query(Account).filter(Account.email == email).first()

    def create_account(self, name: str, email: str, password: str) -> Account:
        account = Account(name=name, email=email, password=password)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account