# Epic Title: FastAPI Backend for Service Modification Requests

from backend.service_modifications.repositories.service_modification_repository import ServiceModificationRepository
import logging

class ServiceModificationService:
    def __init__(self):
        self.repository = ServiceModificationRepository()

    async def process_service_modification(self, request):
        logger = logging.getLogger(__name__)
        logger.info("Processing service modification request asynchronously")

        # Validate request data
        if not self.validate_request(request):
            logger.error("Validation failed for service modification request")
            return {"success": False, "error": "Invalid request data"}

        # Apply modification
        try:
            await self.repository.apply_modification(request)
            return {"success": True}
        except Exception as e:
            logger.error(f"Exception during service modification: {e}")
            return {"success": False, "error": "Failed to apply service modification"}

    def validate_request(self, request):
        return bool(request.service_name and request.modification_details)