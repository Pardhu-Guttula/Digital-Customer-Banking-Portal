# Epic Title: Develop React UI for Submitting Service Modification Requests

from fastapi import APIRouter, HTTPException, status
from backend.service_modifications.services.service_modifications_service import ServiceModificationsService
from backend.service_modifications.models.service_modification_request import ServiceModificationRequest
import logging

router = APIRouter()
service = ServiceModificationsService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/submit_modification_request")
async def submit_modification_request(request: ServiceModificationRequest):
    logger.info("Processing service modification request")
    try:
        service.process_service_modification_request(request)
        return {"message": "Service modification request submitted successfully"}
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")