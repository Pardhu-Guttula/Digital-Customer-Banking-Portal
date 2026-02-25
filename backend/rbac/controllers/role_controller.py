# Epic Title: Implement Role-Based Access Controls for User Authorization

from fastapi import APIRouter, Depends, HTTPException, status
from backend.rbac.services.role_service import RoleService
from backend.rbac.models.role import Role
from backend.rbac.models.permission import Permission
import logging

router = APIRouter()
service = RoleService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/roles/{user_id}")
async def get_user_role(user_id: int):
    logger.info(f"Fetching role for user_id: {user_id}")
    try:
        role = service.get_user_role(user_id)
        if not role:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
        return role
    except Exception as e:
        logger.error(f"Error fetching role for user_id {user_id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.get("/permissions/{role_id}")
async def get_role_permissions(role_id: int):
    logger.info(f"Fetching permissions for role_id: {role_id}")
    try:
        permissions = service.get_role_permissions(role_id)
        return permissions
    except Exception as e:
        logger.error(f"Error fetching permissions for role_id {role_id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")