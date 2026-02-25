# Epic Title: Save Incomplete Applications

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, ValidationError
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
        logger.error(f"Validation error: {e.errors()}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.errors())
    except Exception as e:
        logger.error(f"Error saving application: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")