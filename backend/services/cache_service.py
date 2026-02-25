# Epic Title: Personalized User Dashboard for Banking Products and Services

import redis
import logging

class CacheService:
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0)
    
    def get(self, key: str):
        try:
            data = self.client.get(key)
            if data:
                return eval(data)
        except redis.RedisError as e:
            logger.error(f"Redis error: {e}")
        return None

    def set(self, key: str, value: dict):
        try:
            self.client.set(key, str(value))
        except redis.RedisError as e:
            logger.error(f"Redis error: {e}")