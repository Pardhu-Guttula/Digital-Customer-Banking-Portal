# Epic Title: Capture and maintain a history of user interactions

from sqlalchemy.orm import Session

class UserInteractionRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save_interaction(self, data: dict):
        query = """
            INSERT INTO user_interactions (user_id, action, timestamp)
            VALUES (:user_id, :action, :timestamp)
        """
        self.db_session.execute(query, data)
        self.db_session.commit()