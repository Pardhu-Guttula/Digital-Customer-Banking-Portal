# Epic Title: FastAPI Backend for Service Modification Requests

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from backend.service_modifications.services.service_modification_service import ServiceModificationService
import logging

router = APIRouter()
service = ServiceModificationService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ServiceModificationRequest(BaseModel):
    service_name: constr(min_length=1)
    modification_details: constr(min_length=1)
    

@router.post("/service_modifications")
async def submit_service_modification(request: ServiceModificationRequest):
    logger.info(f"Received service modification request: {request}")

    # Validate input
    if not request.service_name or not request.modification_details:
        raise HTTPException(status_code=400, detail="service_name and modification_details are required")

    try:
        result = await service.process_service_modification(request)
        if not result['success']:
            raise HTTPException(status_code=400, detail=result['error'])
        return {"message": "Service modification applied successfully"}
    except Exception as e:
        logger.error(f"Backend service error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")