# File: tests/test_role.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask, jsonify
from backend.access_control.services.role_service import RoleService
from backend.database.config import get_db
import role_bp

class RoleBlueprintTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(role_bp.role_bp)
        self.client = self.app.test_client()

    @patch('role_bp.get_db')
    @patch('role_bp.RoleService')
    def test_create_role_success(self, MockRoleService, mock_get_db):
        mock_db = Mock()
        mock_get_db.return_value = iter([mock_db])
        mock_role_service = MockRoleService.return_value
        mock_role_service.create_role.return_value = None

        response = self.client.post('/roles', json={'name': 'admin'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {'message': 'Role created successfully'})
        mock_role_service.create_role.assert_called_once_with({'name': 'admin'})

    @patch('role_bp.get_db')
    @patch('role_bp.RoleService')
    def test_create_role_failure(self, MockRoleService, mock_get_db):
        mock_db = Mock()
        mock_get_db.return_value = iter([mock_db])
        mock_role_service = MockRoleService.return_value
        mock_role_service.create_role.side_effect = Exception('Role creation failed')

        response = self.client.post('/roles', json={})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Role creation failed'})
        mock_role_service.create_role.assert_called_once_with({})

    @patch('role_bp.get_db')
    @patch('role_bp.RoleService')
    def test_get_roles_success(self, MockRoleService, mock_get_db):
        mock_db = Mock()
        mock_get_db.return_value = iter([mock_db])
        mock_role_service = MockRoleService.return_value
        mock_role_service.get_roles.return_value = [{'name': 'admin'}, {'name': 'user'}]

        response = self.client.get('/roles')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'roles': [{'name': 'admin'}, {'name': 'user'}]})
        mock_role_service.get_roles.assert_called_once()

    @patch('role_bp.get_db')
    @patch('role_bp.RoleService')
    def test_get_roles_empty(self, MockRoleService, mock_get_db):
        mock_db = Mock()
        mock_get_db.return_value = iter([mock_db])
        mock_role_service = MockRoleService.return_value
        mock_role_service.get_roles.return_value = []

        response = self.client.get('/roles')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'roles': []})
        mock_role_service.get_roles.assert_called_once()