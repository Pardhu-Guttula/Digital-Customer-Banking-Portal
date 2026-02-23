# Epic Title: Integrate with PostgreSQL for Data Storage

from sqlalchemy import Column, Integer, String, TIMESTAMP
from backend.database.config import Base

class Backup(Base):
    __tablename__ = "backups"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)