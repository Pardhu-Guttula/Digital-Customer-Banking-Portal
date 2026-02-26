# File: tests/test_service_modification_repository.py

import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from service_modification_repository import ServiceModificationRepository

class TestServiceModificationRepository(unittest.TestCase):

    def setUp(self):
        self.mock_session = MagicMock(spec=Session)
        self.repo = ServiceModificationRepository(self.mock_session)

    def test_save_service_modification_request_success(self):
        data = {
            "service_name": "TestService",
            "modification_details": "Update configuration",
            "user_id": 12345
        }
        self.repo.save_service_modification_request(data)
        query = """
            INSERT INTO service_modification_requests (service_name, modification_details, user_id, timestamp)
            VALUES (:service_name, :modification_details, :user_id, NOW())
        """
        self.mock_session.execute.assert_called_once_with(query, data)
        self.mock_session.commit.assert_called_once()

    def test_save_service_modification_request_empty_data(self):
        data = {}
        with self.assertRaises(KeyError):
            self.repo.save_service_modification_request(data)

    def test_save_service_modification_request_partial_data(self):
        data = {
            "service_name": "TestService"
        }
        with self.assertRaises(KeyError):
            self.repo.save_service_modification_request(data)

    def test_save_service_modification_request_missing_user_id(self):
        data = {
            "service_name": "TestService",
            "modification_details": "Update configuration",
        }
        with self.assertRaises(KeyError):
            self.repo.save_service_modification_request(data)

    def test_save_service_modification_request_invalid_data_type(self):
        data = "Invalid data type"
        with self.assertRaises(TypeError):
            self.repo.save_service_modification_request(data)

    def test_save_service_modification_request_null_handling(self):
        data = None
        with self.assertRaises(TypeError):
            self.repo.save_service_modification_request(data)

if __name__ == '__main__':
    unittest.main()
