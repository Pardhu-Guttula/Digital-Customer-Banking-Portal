# Epic Title: Secure Login System with MFA

from sqlalchemy.orm import Session
from backend.authentication.models.mfa_setup import MFASetup
from backend.authentication.models.token import Token

class MFARepository:
    def __init__(self, db: Session):
        self.db = db

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