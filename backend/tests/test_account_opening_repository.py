# Epic Title: Store Account Opening Request Details in PostgreSQL

import unittest
from backend.account_opening.models.account_opening_request import AccountOpeningRequest
from backend.account_opening.repositories.account_opening_repository import AccountOpeningRepository

class TestAccountOpeningRepository(unittest.TestCase):

    def setUp(self):
        self.repository = AccountOpeningRepository()
        
    def test_save_account_opening_request(self):
        request = AccountOpeningRequest(name="Jane Doe", email="jane.doe@example.com", phone="0987654321", address="456 Another St")
        
        try:
            self.repository.save_account_opening_request(request)
        except Exception:
            self.fail("Saving account opening request failed with valid data")

    def test_save_account_opening_request_with_invalid_data(self):
        invalid_request = AccountOpeningRequest(name="", email="bad-email", phone="123", address="")
        
        with self.assertRaises(Exception):
            self.repository.save_account_opening_request(invalid_request)

if __name__ == "__main__":
    unittest.main()