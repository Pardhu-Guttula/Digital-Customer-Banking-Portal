# Epic Title: Save Incomplete Applications

from backend.incomplete_applications.repositories.application_repository import ApplicationRepository
import logging

class ApplicationService:
    def __init__(self):
        self.repository = ApplicationRepository()

    def save_application(self, data: dict):
        logger = logging.getLogger(__name__)
        logger.info("Saving application data")

        # Validate data integrity
        if not self.validate_data(data):
            logger.error("Data integrity validation failed")
            raise ValueError("Invalid application data")

        # Save application data
        self.repository.save_application(data)

    def validate_data(self, data: dict) -> bool:
        required_fields = ['user_id', 'application_data']
        for field in required_fields:
            if field not in data or not data[field]:
                return False
        return True