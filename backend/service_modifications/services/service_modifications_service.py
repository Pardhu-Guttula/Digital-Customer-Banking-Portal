# Epic Title: Integrate PostgreSQL for Storing Service Modification Request Details

from backend.service_modifications.repositories.service_modifications_repository import ServiceModificationsRepository
from backend.service_modifications.models.service_modification_request import ServiceModificationRequest
import logging

class ServiceModificationsService:
    def __init__(self):
        self.repository = ServiceModificationsRepository()

    def process_save_request(self, request: ServiceModificationRequest):
        try:
            self.repository.save_modification_request(request)
        except ValueError as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Validation failed for the service modification request: {e}")
            raise ValueError("Invalid request data")
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Error processing request: {e}")
            raise

    def process_retrieve_request(self):
        try:
            return self.repository.retrieve_modification_requests()
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Error processing retrieval: {e}")
            raise

    def validate_request(self, request: ServiceModificationRequest) -> bool:
        if not request.user_id or not request.service_type or not request.modification_details:
            return False
        return True