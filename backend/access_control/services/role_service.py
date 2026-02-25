# Epic Title: Implement role-based access control for user authorization

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

    def assign_permissions_to_role(self, role_name: str, permissions: list):
        if not role_name or not permissions:
            raise ValueError("Missing role name or permissions")
        self.role_repository.assign_permissions_to_role(role_name, permissions)

    def assign_role_to_user(self, user_id: int, role_name: str):
        if not user_id or not role_name:
            raise ValueError("Missing user ID or role name")
        self.role_repository.assign_role_to_user(user_id, role_name)
