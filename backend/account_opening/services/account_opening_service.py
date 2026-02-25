# Epic Title: PostgreSQL Data Storage for Account Opening Requests

from backend.account_opening.repositories.account_opening_repository import AccountOpeningRepository
import logging

class AccountOpeningService:
    def __init__(self):
        self.repository = AccountOpeningRepository()

    def process_request(self, data: dict):
        logger = logging.getLogger(__name__)
        logger.info("Processing account opening request")

        # Validate data integrity
        if not self.validate_data(data):
            logger.error("Data integrity validation failed")
            return None, "Invalid request data"

        # Attempt to store in PostgreSQL
        try:
            self.repository.store_request(data)
        except Exception as e:
            logger.error(f"Exception during data storage: {e}")
            return None, "Failed to store account opening request"

        logger.info("Successfully processed account opening request")
        return "success", None

    def validate_data(self, data: dict):
        required_fields = ['name', 'email', 'phone', 'address']
        for field in required_fields:
            if field not in data or not data[field]:
                return False
        return True