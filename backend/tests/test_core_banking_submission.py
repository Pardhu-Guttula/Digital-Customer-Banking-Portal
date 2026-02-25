# Epic Title: Develop Backend Process Workflows using FastAPI

import unittest
from backend.account_opening.models.account_opening_request import AccountOpeningRequest
from backend.integration.core_banking.services.core_banking_service import CoreBankingService

class TestCoreBankingSubmission(unittest.TestCase):

    def setUp(self):
        self.service = CoreBankingService()

    def test_successful_request_submission(self):
        request = AccountOpeningRequest(name="Jane Doe", email="jane.doe@example.com", phone="0987654321", address="456 Another St")
        
        try:
            self.service.process_account_opening_request(request)
        except Exception:
            self.fail("Request submission to core banking failed with valid data")

    def test_request_validation_failure(self):
        invalid_request = AccountOpeningRequest(name="", email="bad-email", phone="123", address="")
        
        with self.assertRaises(ValueError):
            self.service.process_account_opening_request(invalid_request)

    def test_request_submission_error_handling(self):
        invalid_request = AccountOpeningRequest(name="Jane Doe", email="jane.doe@example.com", phone="0987654321", address="456 Another St")
        
        with self.assertRaises(Exception):
            self.service.process_account_opening_request(invalid_request)

if __name__ == "__main__":
    unittest.main()