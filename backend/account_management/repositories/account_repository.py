# Epic Title: Develop streamlined workflows for submitting account opening requests

from sqlalchemy.orm import Session

class AccountRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save_account_opening_request(self, data: dict):
        query = """
            INSERT INTO account_opening_requests (name, email, phone, address, income)
            VALUES (:name, :email, :phone, :address, :income)
        """
        self.db_session.execute(query, data)
        self.db_session.commit()