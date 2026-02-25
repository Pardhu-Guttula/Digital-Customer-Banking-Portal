# Epic Title: Implement Role-Based Access Controls for User Authorization

from backend.rbac.repositories.role_repository import RoleRepository
import logging

class RoleService:
    def __init__(self):
        self.repository = RoleRepository()

    def get_user_role(self, user_id: int) -> dict:
        logger = logging.getLogger(__name__)
        logger.info(f"Retrieving role for user_id: {user_id}")
        return self.repository.get_user_role(user_id)

    def get_role_permissions(self, role_id: int) -> list:
        logger = logging.getLogger(__name__)
        logger.info(f"Retrieving permissions for role_id: {role_id}")
        return self.repository.get_role_permissions(role_id)