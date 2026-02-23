# Epic Title: Security Measures for API Integration

from sqlalchemy.orm import Session

class SecurityRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def verify_token(self, token: str) -> bool:
        query = "SELECT COUNT(*) FROM authorized_tokens WHERE token = :token"
        result = self.db_session.execute(query, {'token': token}).fetchone()
        return bool(result[0])