# File: tests/test_permission_service.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from backend.access_control.services.permission_service import PermissionService
from backend.database.config import get_db

class TestPermissionService(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        self.app.config["TESTING"] = True

    @patch('backend.access_control.services.permission_service.PermissionService.assign_permission')
    @patch('backend.database.config.get_db')
    def test_assign_permission_to_role_success(self, mock_get_db, mock_assign_permission):
        db_mock = MagicMock()
        mock_get_db.return_value = iter([db_mock])
        mock_assign_permission.return_value = None

        data = {
            'role_id': 1,
            'permissions': ['read', 'write']
        }

        response = self.client.post('/permissions', data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Permissions assigned successfully"})

    @patch('backend.access_control.services.permission_service.PermissionService.assign_permission')
    @patch('backend.database.config.get_db')
    def test_assign_permission_to_role_failure(self, mock_get_db, mock_assign_permission):
        db_mock = MagicMock()
        mock_get_db.return_value = iter([db_mock])
        mock_assign_permission.side_effect = Exception("Failed to assign permissions")

        data = {
            'role_id': 1,
            'permissions': ['read', 'write']
        }

        response = self.client.post('/permissions', data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Failed to assign permissions"})

    @patch('backend.database.config.get_db')
    def test_assign_permission_with_invalid_data(self, mock_get_db):
        db_mock = MagicMock()
        mock_get_db.return_value = iter([db_mock])
        # No data provided

        response = self.client.post('/permissions', data=json.dumps({}), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    @patch('backend.database.config.get_db')
    def test_assign_permission_with_null_data(self, mock_get_db):
        db_mock = MagicMock()
        mock_get_db.return_value = iter([db_mock])

        response = self.client.post('/permissions', data=None, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()