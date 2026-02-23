# Epic Title: Track and Analyze User Behavior

from sqlalchemy import Column, Integer, String, TIMESTAMP
from backend.database.config import Base

class UserBehavior(Base):
    __tablename__ = 'user_behavior'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    action = Column(String, nullable=False)
    detail = Column(String)
    timestamp = Column(TIMESTAMP, nullable=False)