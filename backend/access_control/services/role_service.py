# Epic Title: Managing user roles and permissions

from backend.access_control.repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self, db):
        self.role_repository = RoleRepository(db)

    def create_role(self, data: dict):
        role_name = data.get('role_name')
        if not role_name:
            raise ValueError("Missing role name")
        self.role_repository.create_role(role_name)

    def get_roles(self):
        return self.role_repository.get_roles()