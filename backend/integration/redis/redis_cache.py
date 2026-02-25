# Epic Title: Redis Caching for Account Opening Requests

import redis
import logging

class RedisCache:
    def __init__(self):
        self.redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)

    def cache_data(self, data: dict):
        logger = logging.getLogger(__name__)
        key = data['email']
        value = str(data)
        
        try:
            self.redis_instance.set(key, value)
            logger.info(f"Data cached in Redis: {data}")
        except Exception as e:
            logger.error(f"Error caching data in Redis: {e}")
            raise