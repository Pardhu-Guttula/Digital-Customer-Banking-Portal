# Epic Title: Integrate Self-Service Portal with Core Banking System

from fastapi import APIRouter, HTTPException, status
from backend.integration.core_banking.services.integration_service import IntegrationService
import logging

router = APIRouter()
service = IntegrationService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/integration/sync")
async def sync_data():
    logger.info("Starting data sync between PostgreSQL and core banking system")
    try:
        service.sync_data()
        return {"message": "Data sync completed successfully"}
    except Exception as e:
        logger.error(f"Error during data sync: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")