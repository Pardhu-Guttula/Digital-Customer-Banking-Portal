# Epic Title: Implement Caching of Temporary Data in Redis

import redis
import logging

class CacheRepository:
    def __init__(self):
        self.client = redis.StrictRedis(host="localhost", port=6379, db=0)

    def cache_data(self, key: str, data: dict):
        logger = logging.getLogger(__name__)
        try:
            self.client.set(key, data)
            logger.info(f"Data cached with key: {key}")
        except redis.RedisError as e:
            logger.error(f"Failed to cache data: {e}")
            raise