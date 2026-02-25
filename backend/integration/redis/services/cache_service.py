# Epic Title: Implement Caching of Temporary Data in Redis

from backend.integration.redis.repositories.cache_repository import CacheRepository
from backend.account_opening.models.account_opening_request import AccountOpeningRequest
import logging

class CacheService:
    def __init__(self):
        self.repository = CacheRepository()

    def cache_account_opening_request(self, request: AccountOpeningRequest):
        logger = logging.getLogger(__name__)
        if not self.validate_request(request):
            logger.error("Invalid account opening request data")
            raise ValueError("Invalid data provided")

        self.repository.cache_data(request.email, request.dict())
        logger.info("Account opening request cached successfully")

    def validate_request(self, request: AccountOpeningRequest) -> bool:
        # Add data consistency validation logic here
        return True