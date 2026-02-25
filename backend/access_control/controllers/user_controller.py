# Epic Title: Enforce Role-Based Access Control Using FastAPI

from fastapi import APIRouter, Depends, HTTPException, status
from backend.access_control.services.role_service import RoleService
from backend.access_control.dependencies import get_current_user
import logging

router = APIRouter()
service = RoleService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/user/data")
async def get_user_data(current_user: dict = Depends(get_current_user)):
    try:
        data = service.get_user_data(current_user['role'])
        return data
    except Exception as e:
        logger.error(f"Error retrieving user data: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")