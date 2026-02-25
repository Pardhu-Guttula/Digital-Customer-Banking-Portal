# Epic Title: Real-time Status Updates Using React and Redis

import redis
import logging

class RedisCache:
    def __init__(self):
        self.redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)

    def cache_data(self, key: int, value: str):
        logger = logging.getLogger(__name__)
        try:
            self.redis_instance.set(key, value)
            logger.info(f"Cached data in Redis: {key} -> {value}")
        except Exception as e:
            logger.error(f"Error caching data in Redis: {e}")
            raise

    def retrieve_data(self, key: int):
        logger = logging.getLogger(__name__)
        try:
            value = self.redis_instance.get(key)
            if value:
                logger.info(f"Data retrieved from Redis for key {key}")
                return value.decode('utf-8')
            else:
                logger.info(f"No data found in Redis for key {key}")
                return None
        except Exception as e:
            logger.error(f"Error retrieving data from Redis: {e}")
            raise

    def evict_cache(self, key: int):
        logger = logging.getLogger(__name__)
        try:
            self.redis_instance.delete(key)
            logger.info(f"Cache evicted for key {key}")
        except Exception as e:
            logger.error(f"Error evicting cache for key {key}: {e}")
            raise