# Epic Title: Backend API Development with FastAPI

from backend.realtime_status_updates.repositories.status_update_repository import StatusUpdateRepository
from backend.integration.redis.redis_cache import RedisCache
import logging

class StatusUpdateService:
    def __init__(self):
        self.repository = StatusUpdateRepository()
        self.cache = RedisCache()

    def get_status_from_cache(self, request_id: int):
        logger = logging.getLogger(__name__)
        status = self.cache.retrieve_data(request_id)
        if status:
            logger.info(f"Status retrieved from cache for request ID: {request_id}")
        return status

    def get_status_from_db(self, request_id: int):
        logger = logging.getLogger(__name__)
        status = self.repository.fetch_status(request_id)
        if status:
            self.cache.cache_data(request_id, status)
            logger.info(f"Status retrieved from DB and cached for request ID: {request_id}")
        return status