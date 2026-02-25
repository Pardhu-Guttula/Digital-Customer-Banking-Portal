# Epic Title: Backend Process Workflows for Account Opening

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.application.services.account_opening_service import AccountOpeningService
import logging

router = APIRouter()
account_opening_service = AccountOpeningService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AccountOpeningRequest(BaseModel):
    name: str
    email: str
    phone: str
    address: str

@router.post("/account_opening")
async def submit_account_opening(request: AccountOpeningRequest):
    logger.info("Received account opening request")
    try:
        result, error = account_opening_service.process_request(request)
        if error:
            raise HTTPException(status_code=400, detail=error)
        return {"message": "Successfully submitted to core banking system"}
    except Exception as e:
        logger.error(f"Error processing account opening request: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")