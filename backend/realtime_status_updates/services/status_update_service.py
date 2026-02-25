# Epic Title: Real-time Status Updates Using React and Redis

from backend.realtime_status_updates.repositories.status_update_repository import StatusUpdateRepository
from backend.integration.redis.redis_cache import RedisCache
import logging

class StatusUpdateService:
    def __init__(self):
        self.repository = StatusUpdateRepository()
        self.cache = RedisCache()

    def get_status_from_cache(self, request_id: int):
        logger = logging.getLogger(__name__)
        logger.info(f"Trying to get status from cache for request ID: {request_id}")
        return self.cache.retrieve_data(request_id)

    def get_status_from_db(self, request_id: int):
        logger = logging.getLogger(__name__)
        logger.info(f"Trying to get status from database for request ID: {request_id}")
        status = self.repository.fetch_status(request_id)
        self.cache.cache_data(request_id, status)
        return status