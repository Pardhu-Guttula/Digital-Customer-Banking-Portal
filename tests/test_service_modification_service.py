# File: tests/test_service_modification_service.py
import unittest
from unittest.mock import MagicMock, patch
from service_modification_service import ServiceModificationService

class TestServiceModificationService(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_repo = MagicMock()
        self.service = ServiceModificationService(self.mock_db)
        self.service.service_modification_repository = self.mock_repo

    def test_process_modification_request_successful(self):
        data = {"service_name": "Service A", "modification_details": "Details"}
        self.mock_repo.save_service_modification_request.return_value = None
        result = self.service.process_modification_request(data)
        self.assertEqual(result, {"success": True, "message": "Request processed"})
        self.mock_repo.save_service_modification_request.assert_called_once_with(data)

    def test_process_modification_request_missing_service_name(self):
        data = {"modification_details": "Details"}
        result = self.service.process_modification_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: service_name"})
        self.mock_repo.save_service_modification_request.assert_not_called()

    def test_process_modification_request_missing_modification_details(self):
        data = {"service_name": "Service A"}
        result = self.service.process_modification_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: modification_details"})
        self.mock_repo.save_service_modification_request.assert_not_called()

    def test_process_modification_request_empty_service_name(self):
        data = {"service_name": "", "modification_details": "Details"}
        result = self.service.process_modification_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: service_name"})
        self.mock_repo.save_service_modification_request.assert_not_called()

    def test_process_modification_request_empty_modification_details(self):
        data = {"service_name": "Service A", "modification_details": ""}
        result = self.service.process_modification_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: modification_details"})
        self.mock_repo.save_service_modification_request.assert_not_called()

    def test_process_modification_request_backend_exception(self):
        data = {"service_name": "Service A", "modification_details": "Details"}
        self.mock_repo.save_service_modification_request.side_effect = Exception("DB Error")
        result = self.service.process_modification_request(data)
        self.assertEqual(result, {"success": False, "message": "Backend processing error"})
        self.mock_repo.save_service_modification_request.assert_called_once_with(data)

if __name__ == '__main__':
    unittest.main()