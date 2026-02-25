# Epic Title: Secure Role-Based Data Segregation in PostgreSQL

from fastapi import APIRouter, HTTPException, status, Depends
from backend.rbac.services.data_service import DataService
from backend.access_control.dependencies import get_current_user
import logging

router = APIRouter()
service = DataService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/data")
async def get_data(current_user: dict = Depends(get_current_user)):
    try:
        data = service.get_data_for_role(current_user['role'])
        return {"data": data}
    except Exception as e:
        logger.error(f"Error retrieving data: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.post("/data")
async def create_data(data: str, current_user: dict = Depends(get_current_user)):
    try:
        service.insert_data(data, current_user['role'])
        return {"message": "Data inserted successfully"}
    except Exception as e:
        logger.error(f"Error inserting data: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")