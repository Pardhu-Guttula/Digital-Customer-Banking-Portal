# Epic Title: Redis Caching for Account Opening Requests

from backend.account_opening.repositories.account_opening_repository import AccountOpeningRepository
from backend.integration.core_banking.core_banking_integration import CoreBankingIntegration
from backend.integration.redis.redis_cache import RedisCache
import logging

class AccountOpeningService:
    def __init__(self):
        self.repository = AccountOpeningRepository()
        self.core_banking_integration = CoreBankingIntegration()
        self.redis_cache = RedisCache()

    def process_request(self, data: dict):
        logger = logging.getLogger(__name__)
        logger.info("Processing account opening request")
        
        # Validate data integrity
        if not self.validate_data(data):
            logger.error("Data integrity validation failed")
            return None, "Invalid request data"
        
        # Cache temporary data in Redis
        try:
            self.redis_cache.cache_data(data)
            logger.info("Cached temporary data in Redis successfully")
        except Exception as e:
            logger.error(f"Error caching data in Redis: {e}")
            return None, "Failed to cache temporary data"
        
        # Attempt to store in PostgreSQL
        try:
            self.repository.store_request(data)
        except Exception as e:
            logger.error(f"Exception during data storage: {e}")
            return None, "Failed to store account opening request"
        
        # Attempt to submit to core banking system
        try:
            response, error = self.core_banking_integration.submit_request(data)
            if error:
                logger.error("Error from core banking system")
                return None, "Core banking system error"
        except Exception as e:
            logger.error(f"Exception during core banking submission: {e}")
            return None, "Failed to submit request to core banking system"
        
        return "success", None

    def validate_data(self, data: dict):
        required_fields = ['name', 'email', 'phone', 'address']
        for field in required_fields:
            if field not in data or not data[field]:
                return False
        return True