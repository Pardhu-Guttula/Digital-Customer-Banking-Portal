# Epic Title: Save incomplete application state

from sqlalchemy.orm import Session

class ApplicationStateRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save_state(self, data: dict):
        query = """
            REPLACE INTO application_states (user_id, state)
            VALUES (:user_id, :state)
        """
        self.db_session.execute(query, data)
        self.db_session.commit()

    def load_state(self, user_id: str) -> str:
        query = "SELECT state FROM application_states WHERE user_id = :user_id"
        result = self.db_session.execute(query, {'user_id': user_id}).fetchone()
        return result['state'] if result else ""