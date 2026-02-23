# Epic Title: Implement role-based access control for user authorization

from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def assign_role(self, user_id: str, role: str):
        query = "UPDATE users SET role_id = (SELECT id FROM roles WHERE name = :role) WHERE id = :user_id"
        self.db_session.execute(query, {'role': role, 'user_id': user_id})
        self.db_session.commit()

    def get_user_permissions(self, user_id: str):
        query = """
            SELECT p.permission FROM role_permissions p
            JOIN users u ON u.role_id = p.role_id
            WHERE u.id = :user_id
        """
        result = self.db_session.execute(query, {'user_id': user_id}).fetchall()
        return [row['permission'] for row in result]