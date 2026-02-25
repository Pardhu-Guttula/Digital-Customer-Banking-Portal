# Epic Title: Enable Users to Submit Account Opening Requests through Streamlined Workflows

import unittest
from backend.account_opening.models.account_opening_request import AccountOpeningRequest
from backend.account_opening.services.account_opening_service import AccountOpeningService

class TestAccountOpening(unittest.TestCase):

    def setUp(self):
        self.service = AccountOpeningService()

    def test_successful_account_opening_request(self):
        request = AccountOpeningRequest(name="John Doe", email="john.doe@example.com", phone="1234567890", address="123 Main St")
        try:
            self.service.process_account_opening_request(request)
        except ValueError:
            self.fail("Account opening request failed with valid data")

    def test_account_opening_request_validation_failure(self):
        invalid_request = AccountOpeningRequest(name="", email="bad-email", phone="123", address="")
        with self.assertRaises(ValueError):
            self.service.process_account_opening_request(invalid_request)

if __name__ == "__main__":
    unittest.main()