# File: tests/test_role_routes.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from backend.access_control.blueprints.role import role_bp

class RoleRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(role_bp)
        self.client = self.app.test_client()

    @patch('backend.access_control.blueprints.role.get_db')
    @patch('backend.access_control.blueprints.role.RoleService.create_role')
    def test_create_role_success(self, mock_create_role, mock_get_db):
        mock_db = MagicMock()
        mock_get_db.return_value = iter([mock_db])
        mock_create_role.return_value = None

        response = self.client.post('/roles', json={"name": "admin"})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"message": "Role created successfully"})
        mock_create_role.assert_called_once_with({"name": "admin"})

    @patch('backend.access_control.blueprints.role.get_db')
    @patch('backend.access_control.blueprints.role.RoleService.create_role')
    def test_create_role_failure(self, mock_create_role, mock_get_db):
        mock_db = MagicMock()
        mock_get_db.return_value = iter([mock_db])
        mock_create_role.side_effect = Exception("Role creation failed")

        response = self.client.post('/roles', json={"name": "admin"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {"error": "Role creation failed"})
        mock_create_role.assert_called_once_with({"name": "admin"})

    @patch('backend.access_control.blueprints.role.get_db')
    @patch('backend.access_control.blueprints.role.RoleService.get_roles')
    def test_get_roles_success(self, mock_get_roles, mock_get_db):
        mock_db = MagicMock()
        mock_get_db.return_value = iter([mock_db])
        mock_get_roles.return_value = [{"name": "admin"}]

        response = self.client.get('/roles')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"roles": [{"name": "admin"}]})
        mock_get_roles.assert_called_once()

if __name__ == '__main__':
    unittest.main()