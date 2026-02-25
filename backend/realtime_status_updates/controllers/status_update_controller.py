# Epic Title: Backend API Development with FastAPI

from fastapi import APIRouter, HTTPException
from backend.realtime_status_updates.services.status_update_service import StatusUpdateService
import logging

router = APIRouter()
service = StatusUpdateService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/status/{request_id}")
async def get_status_update(request_id: int):
    logger.info(f"Fetching status update for request ID: {request_id}")
    try:
        status = service.get_status_from_cache(request_id)
        if status is None:
            status = service.get_status_from_db(request_id)
        if status is None:
            raise HTTPException(status_code=404, detail="Request ID not found")
        return {"request_id": request_id, "status": status}
    except HTTPException as e:
        logger.error(f"HTTP error: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Internal server error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")