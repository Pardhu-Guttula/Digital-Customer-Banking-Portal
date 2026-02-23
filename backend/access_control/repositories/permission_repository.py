# Epic Title: Managing user roles and permissions

from sqlalchemy.orm import Session

class PermissionRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def assign_permission(self, role: str, permissions: list):
        query = "INSERT INTO role_permissions (role_id, permission) VALUES (:role_id, :permission)"
        role_id_query = "SELECT id FROM roles WHERE name = :role"
        role_id_result = self.db_session.execute(role_id_query, {'role': role}).fetchone()
        role_id = role_id_result['id']
        
        for permission in permissions:
            self.db_session.execute(query, {'role_id': role_id, 'permission': permission})
        self.db_session.commit()