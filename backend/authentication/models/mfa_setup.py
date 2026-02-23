# Epic Title: Secure Login System with MFA

from sqlalchemy import Column, Integer, String, Boolean
from backend.database.config import Base

class MFASetup(Base):
    __tablename__ = 'mfa_setup'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, nullable=False)
    mfa_method = Column(String, nullable=False)  # Options: 'SMS', 'Email'
    is_active = Column(Boolean, default=True)