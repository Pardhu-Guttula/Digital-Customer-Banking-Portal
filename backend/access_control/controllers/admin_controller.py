# Epic Title: Enforce Role-Based Access Control Using FastAPI

from fastapi import APIRouter, Depends, HTTPException, status
from backend.access_control.services.role_service import RoleService
from backend.access_control.dependencies import get_current_user
import logging

router = APIRouter()
service = RoleService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/admin/data")
async def get_admin_data(current_user: dict = Depends(get_current_user)):
    if current_user['role'] != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
    
    try:
        data = service.get_admin_data()
        return data
    except Exception as e:
        logger.error(f"Error retrieving admin data: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")