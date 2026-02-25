# Epic Title: Enforce Role-Based Access Control Using FastAPI

import logging

class RoleService:
    def __init__(self):
        pass

    def get_admin_data(self) -> dict:
        logger = logging.getLogger(__name__)
        logger.info("Retrieving data for admin")
        return {"data": "This is admin specific data"}

    def get_user_data(self, role: str) -> dict:
        logger = logging.getLogger(__name__)
        logger.info(f"Retrieving data for role: {role}")
        if role == 'basic':
            return {"data": "This is basic user data"}
        raise ValueError("Invalid role")