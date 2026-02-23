# Epic Title: Multi-Factor Authentication Setup

from sqlalchemy.orm import Session
from backend.authentication.models.mfa_setup import MFASetup
from backend.authentication.models.token import Token

class MFARepository:
    def __init__(self, db: Session):
        self.db = db

    def create_mfa_setup(self, account_id: int, mfa_method: str) -> MFASetup:
        mfa_setup = MFASetup(account_id=account_id, mfa_method=mfa_method)
        self.db.add(mfa_setup)
        self.db.commit()
        self.db.refresh(mfa_setup)
        return mfa_setup

    def activate_mfa_setup(self, account_id: int, mfa_method: str) -> None:
        self.db.query(MFASetup).filter(
            MFASetup.account_id == account_id,
            MFASetup.mfa_method == mfa_method
        ).update({"is_active": True})
        self.db.commit()

    def create_token(self, account_id: int, token: str) -> Token:
        mfa_token = Token(account_id=account_id, token=token)
        self.db.add(mfa_token)
        self.db.commit()
        self.db.refresh(mfa_token)
        return mfa_token

    def validate_token(self, account_id: int, token: str) -> bool:
        mfa_token = self.db.query(Token).filter(
            Token.account_id == account_id,
            Token.token == token,
            Token.is_valid == True,
            Token.expires_at >= datetime.utcnow()
        ).first()
        if mfa_token:
            self.db.query(Token).filter(
                Token.id == mfa_token.id
            ).update({"is_valid": False})
            self.db.commit()
            return True
        return False