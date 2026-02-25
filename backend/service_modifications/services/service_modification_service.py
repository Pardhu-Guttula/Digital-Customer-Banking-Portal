# Epic Title: PostgreSQL Integration for Service Modification Requests

from backend.service_modifications.repositories.service_modification_repository import ServiceModificationRepository
import logging

class ServiceModificationService:
    def __init__(self):
        self.repository = ServiceModificationRepository()

    def process_request(self, data: dict):
        logger = logging.getLogger(__name__)
        logger.info("Processing service modification request")

        # Validate data integrity
        if not self.validate_data(data):
            logger.error("Data integrity validation failed")
            return None, "Invalid request data"

        # Attempt to store in PostgreSQL
        try:
            self.repository.store_request(data)
        except Exception as e:
            logger.error(f"Exception during data storage: {e}")
            return None, "Failed to store service modification request"

        logger.info("Successfully processed service modification request")
        return "success", None

    def get_all_requests(self):
        logger = logging.getLogger(__name__)
        logger.info("Retrieving all service modification requests")

        try:
            return self.repository.retrieve_all_requests()
        except Exception as e:
            logger.error(f"Exception during data retrieval: {e}")
            raise

    def validate_data(self, data: dict):
        required_fields = ['service_name', 'modification_details']
        for field in required_fields:
            if field not in data or not data[field]:
                return False
        return True