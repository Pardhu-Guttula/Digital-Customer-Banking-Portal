# Epic Title: Develop React UI for Submitting Service Modification Requests

import unittest
from backend.service_modifications.models.service_modification_request import ServiceModificationRequest
from backend.service_modifications.services.service_modifications_service import ServiceModificationsService

class TestServiceModifications(unittest.TestCase):

    def setUp(self):
        self.service = ServiceModificationsService()

    def test_successful_service_modification_request(self):
        request = ServiceModificationRequest(user_id=1, service_type="Internet", modification_details="Upgrade to premium plan")
        
        try:
            self.service.process_service_modification_request(request)
        except ValueError:
            self.fail("Service modification request failed with valid data")

    def test_service_modification_request_validation_failure(self):
        invalid_request = ServiceModificationRequest(user_id=1, service_type="", modification_details="")
        
        with self.assertRaises(ValueError):
            self.service.process_service_modification_request(invalid_request)

if __name__ == "__main__":
    unittest.main()