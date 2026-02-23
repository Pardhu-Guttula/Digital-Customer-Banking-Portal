# Epic Title: Managing user roles and permissions

from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def assign_role(self, user_id: str, role: str):
        query = "UPDATE users SET role_id = (SELECT id FROM roles WHERE name = :role) WHERE id = :user_id"
        self.db_session.execute(query, {'role': role, 'user_id': user_id})
        self.db_session.commit()