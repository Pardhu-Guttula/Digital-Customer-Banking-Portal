# Epic Title: Redis Caching for Service Modification Workflows

import redis
import logging

class RedisCache:
    def __init__(self):
        self.redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)

    def cache_data(self, data: dict):
        logger = logging.getLogger(__name__)
        key = data['service_name']
        value = str(data)
        
        try:
            self.redis_instance.set(key, value)
            logger.info(f"Data cached in Redis: {data}")
        except Exception as e:
            logger.error(f"Error caching data in Redis: {e}")
            raise

    def retrieve_data(self, key: str):
        logger = logging.getLogger(__name__)
        
        try:
            value = self.redis_instance.get(key)
            if value:
                logger.info(f"Data retrieved from Redis for key {key}")
                return eval(value)
            else:
                logger.info(f"No data found in Redis for key {key}")
                return None
        except Exception as e:
            logger.error(f"Error retrieving data from Redis: {e}")
            raise

    def evict_cache(self, key: str):
        logger = logging.getLogger(__name__)
        
        try:
            self.redis_instance.delete(key)
            logger.info(f"Cache evicted for key {key}")
        except Exception as e:
            logger.error(f"Error evicting cache for key {key}: {e}")
            raise