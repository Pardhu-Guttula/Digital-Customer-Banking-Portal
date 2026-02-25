# Epic Title: Backend Process Workflows for Account Opening

from backend.integration.core_banking.core_banking_integration import CoreBankingIntegration
from pydantic import BaseModel
import logging

class AccountOpeningService:
    def __init__(self):
        self.core_banking_integration = CoreBankingIntegration()

    def process_request(self, request: BaseModel):
        logger = logging.getLogger(__name__)
        logger.info("Processing account opening request")

        # Validate data integrity
        if not self.validate_data(request):
            logger.error("Data integrity validation failed")
            return None, "Invalid request data"

        # Attempt to submit to core banking system
        try:
            response = self.core_banking_integration.submit_request(request)
            if response.get('status') != 'success':
                logger.error("Error from core banking system")
                return None, "Core banking system error"
        except Exception as e:
            logger.error(f"Exception during core banking submission: {e}")
            return None, "Failed to submit request to core banking system"

        logger.info("Successfully processed account opening request")
        return response, None

    def validate_data(self, request: BaseModel):
        # Assuming the request params like `name`, `email` etc. are mandatory and have appropriate values
        return all([request.name, request.email, request.phone, request.address])