# Epic Title: Managing user roles and permissions

from sqlalchemy.orm import Session

class RoleRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_role(self, role_name: str):
        query = "INSERT INTO roles (name) VALUES (:role_name)"
        self.db_session.execute(query, {'role_name': role_name})
        self.db_session.commit()

    def get_roles(self):
        query = "SELECT * FROM roles"
        result = self.db_session.execute(query).fetchall()
        return [{'id': row['id'], 'name': row['name']} for row in result]