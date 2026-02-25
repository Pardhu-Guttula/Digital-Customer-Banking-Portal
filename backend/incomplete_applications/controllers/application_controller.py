# Epic Title: Resume Incomplete Applications

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from backend.incomplete_applications.services.application_service import ApplicationService
import logging

router = APIRouter()
service = ApplicationService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ApplicationData(BaseModel):
    user_id: int
    application_data: dict

@router.post("/applications/save")
async def save_application(data: ApplicationData):
    logger.info(f"Received application data to save: {data}")
    try:
        service.save_application(data.dict())
        return {"message": "Application saved successfully"}
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.errors())
    except Exception as e:
        logger.error(f"Error saving application: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.get("/applications/resume/{user_id}")
async def resume_application(user_id: int):
    logger.info(f"Retrieving application data for user ID: {user_id}")
    try:
        application = service.get_application(user_id)
        if not application:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
        return application
    except Exception as e:
        logger.error(f"Error retrieving application: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")