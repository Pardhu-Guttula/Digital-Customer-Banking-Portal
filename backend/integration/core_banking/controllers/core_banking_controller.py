# Epic Title: Develop Backend Process Workflows using FastAPI

from fastapi import APIRouter, HTTPException, status
from backend.integration.core_banking.services.core_banking_service import CoreBankingService
from backend.account_opening.models.account_opening_request import AccountOpeningRequest
import logging

router = APIRouter()
service = CoreBankingService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/submit_account_request")
async def submit_account_request(request: AccountOpeningRequest):
    logger.info("Processing account opening request for core banking submission")
    try:
        service.process_account_opening_request(request)
        return {"message": "Account opening request submitted to core banking system successfully"}
    except ValueError as e:
        logger.error(f"Error in account opening request: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")