# Epic Title: Managing user roles and permissions

from backend.access_control.repositories.permission_repository import PermissionRepository

class PermissionService:
    def __init__(self, db):
        self.permission_repository = PermissionRepository(db)

    def assign_permission(self, data: dict):
        role = data.get('role')
        permissions = data.get('permissions')
        if not role or not permissions:
            raise ValueError("Missing role or permissions")
        self.permission_repository.assign_permission(role, permissions)