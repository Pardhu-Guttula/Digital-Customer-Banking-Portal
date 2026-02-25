# File: tests/test_user.py

import unittest
from unittest.mock import patch, MagicMock
from backend.access_control.services.user_service import UserService
from backend.database.config import get_db
from flask import Flask
from flask.testing import FlaskClient

class UserBlueprintTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_assign_role_to_user_success(self):
        with patch('backend.access_control.services.user_service.UserService.assign_role') as mock_assign_role:
            mock_assign_role.return_value = None
            with self.app.test_request_context('/users/1/role', json={"role": "admin"}):
                response = self.client.post('/users/1/role', json={"role": "admin"})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json(), {"message": "Role assigned to user successfully"})

    def test_assign_role_to_user_failure(self):
        with patch('backend.access_control.services.user_service.UserService.assign_role') as mock_assign_role:
            mock_assign_role.side_effect = Exception("Error")
            with self.app.test_request_context('/users/1/role', json={"role": "admin"}):
                response = self.client.post('/users/1/role', json={"role": "admin"})
                self.assertEqual(response.status_code, 400)
                self.assertEqual(response.get_json(), {"error": "Error"})

    def test_assign_role_to_user_invalid_input(self):
        with self.app.test_request_context('/users/1/role', json={}):
            response = self.client.post('/users/1/role', json={})
            self.assertEqual(response.status_code, 400)

    def test_get_user_permissions_success(self):
        with patch('backend.access_control.services.user_service.UserService.get_user_permissions') as mock_get_user_permissions:
            mock_get_user_permissions.return_value = ['read', 'write']
            with self.app.test_request_context('/users/1/permissions'):
                response = self.client.get('/users/1/permissions')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json(), {"permissions": ['read', 'write']})

    def test_get_user_permissions_empty(self):
        with patch('backend.access_control.services.user_service.UserService.get_user_permissions') as mock_get_user_permissions:
            mock_get_user_permissions.return_value = []
            with self.app.test_request_context('/users/1/permissions'):
                response = self.client.get('/users/1/permissions')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json(), {"permissions": []})

if __name__ == '__main__':
    unittest.main()