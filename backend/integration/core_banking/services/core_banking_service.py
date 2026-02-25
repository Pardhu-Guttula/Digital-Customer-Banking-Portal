# Epic Title: Develop Backend Process Workflows using FastAPI

from backend.integration.core_banking.repositories.core_banking_repository import CoreBankingRepository
from backend.account_opening.models.account_opening_request import AccountOpeningRequest
import logging

class CoreBankingService:
    def __init__(self):
        self.repository = CoreBankingRepository()

    def process_account_opening_request(self, request: AccountOpeningRequest):
        logger = logging.getLogger(__name__)
        if not self.validate_request(request):
            logger.error("Invalid account opening request data")
            raise ValueError("Invalid data provided")
        
        try:
            self.repository.submit_to_core_banking(request)
            logger.info("Account opening request submitted to core banking successfully")
        except Exception as e:
            logger.error(f"Error submitting to core banking system: {e}")
            raise

    def validate_request(self, request: AccountOpeningRequest) -> bool:
        # Add data integrity validation logic here
        return True