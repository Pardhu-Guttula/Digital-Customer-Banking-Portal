# File: tests/test_account_service.py

import unittest
from unittest.mock import MagicMock, patch
from backend.account_management.services.account_service import AccountService

class TestAccountService(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.account_service = AccountService(self.mock_db)

    def test_process_opening_request_success(self):
        data = {"name": "John", "email": "john@example.com", "phone": "1234567890"}
        self.account_service.account_repository.save_account_opening_request = MagicMock()
        result = self.account_service.process_opening_request(data)
        self.assertEqual(result, {"success": True, "message": "Request processed"})

    def test_process_opening_request_missing_name(self):
        data = {"email": "john@example.com", "phone": "1234567890"}
        result = self.account_service.process_opening_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: name"})

    def test_process_opening_request_missing_email(self):
        data = {"name": "John", "phone": "1234567890"}
        result = self.account_service.process_opening_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: email"})

    def test_process_opening_request_missing_phone(self):
        data = {"name": "John", "email": "john@example.com"}
        result = self.account_service.process_opening_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: phone"})

    def test_process_opening_request_empty_name(self):
        data = {"name": "", "email": "john@example.com", "phone": "1234567890"}
        result = self.account_service.process_opening_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: name"})

    def test_process_opening_request_empty_email(self):
        data = {"name": "John", "email": "", "phone": "1234567890"}
        result = self.account_service.process_opening_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: email"})

    def test_process_opening_request_empty_phone(self):
        data = {"name": "John", "email": "john@example.com", "phone": ""}
        result = self.account_service.process_opening_request(data)
        self.assertEqual(result, {"success": False, "message": "Missing mandatory field: phone"})

    @patch('backend.account_management.repositories.account_repository.AccountRepository.save_account_opening_request')
    def test_process_opening_request_backend_exception(self, mock_save_account_opening_request):
        mock_save_account_opening_request.side_effect = Exception("Backend error")
        data = {"name": "John", "email": "john@example.com", "phone": "1234567890"}
        result = self.account_service.process_opening_request(data)
        self.assertEqual(result, {"success": False, "message": "Backend processing error"})

if __name__ == '__main__':
    unittest.main()