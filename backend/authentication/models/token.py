# Epic Title: Secure Login System with MFA

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from backend.database.config import Base
from datetime import datetime, timedelta

class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, nullable=False)
    token = Column(String, nullable=False)
    is_valid = Column(Boolean, default=True)
    expires_at = Column(DateTime, nullable=False, default=lambda: datetime.utcnow() + timedelta(minutes=15))