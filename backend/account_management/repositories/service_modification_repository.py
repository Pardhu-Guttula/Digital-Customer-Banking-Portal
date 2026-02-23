# Epic Title: Develop streamlined workflows for submitting service modification requests

from sqlalchemy.orm import Session

class ServiceModificationRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save_service_modification_request(self, data: dict):
        query = """
            INSERT INTO service_modification_requests (service_name, modification_details, user_id, timestamp)
            VALUES (:service_name, :modification_details, :user_id, NOW())
        """
        self.db_session.execute(query, data)
        self.db_session.commit()