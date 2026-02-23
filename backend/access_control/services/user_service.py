# Epic Title: Implement role-based access control for user authorization

from backend.access_control.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    def assign_role(self, user_id: str, data: dict):
        role = data.get('role')
        if not role:
            raise ValueError("Missing role")
        self.user_repository.assign_role(user_id, role)

    def get_user_permissions(self, user_id: str):
        return self.user_repository.get_user_permissions(user_id)