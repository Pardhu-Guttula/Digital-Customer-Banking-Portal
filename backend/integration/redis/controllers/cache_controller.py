# Epic Title: Implement Caching of Temporary Data in Redis

from fastapi import APIRouter, HTTPException, status
from backend.integration.redis.services.cache_service import CacheService
from backend.account_opening.models.account_opening_request import AccountOpeningRequest
import logging

router = APIRouter()
service = CacheService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/cache_account_request")
async def cache_account_request(request: AccountOpeningRequest):
    logger.info("Caching account opening request data")
    try:
        service.cache_account_opening_request(request)
        return {"message": "Account opening request cached successfully"}
    except ValueError as e:
        logger.error(f"Error caching account opening request: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")