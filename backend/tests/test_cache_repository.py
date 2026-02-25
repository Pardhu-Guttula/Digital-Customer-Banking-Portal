# Epic Title: Implement Caching of Temporary Data in Redis

import unittest
from backend.account_opening.models.account_opening_request import AccountOpeningRequest
from backend.integration.redis.repositories.cache_repository import CacheRepository

class TestCacheRepository(unittest.TestCase):

    def setUp(self):
        self.repository = CacheRepository()
        
    def test_successful_cache(self):
        request_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890",
            "address": "123 Main St"
        }
        
        try:
            self.repository.cache_data(request_data['email'], request_data)
        except Exception:
            self.fail("Caching account opening request failed with valid data")

    def test_cache_with_invalid_data(self):
        invalid_data = {
            "name": "",
            "email": "bad-email",
            "phone": "123",
            "address": ""
        }
        
        with self.assertRaises(Exception):
            self.repository.cache_data(invalid_data['email'], invalid_data)

if __name__ == "__main__":
    unittest.main()