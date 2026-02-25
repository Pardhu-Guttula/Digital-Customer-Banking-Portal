# File: tests/test_permission_service.py

import unittest
from unittest.mock import MagicMock, patch
from backend.access_control.repositories.permission_repository import PermissionRepository
from backend.access_control.services.permission_service import PermissionService

class TestPermissionService(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.permission_service = PermissionService(self.mock_db)

    def test_assign_permission_success(self):
        self.permission_service.permission_repository.assign_permission = MagicMock()
        data = {'role': 'admin', 'permissions': ['read', 'write']}
        self.permission_service.assign_permission(data)
        self.permission_service.permission_repository.assign_permission.assert_called_once_with('admin', ['read', 'write'])

    def test_assign_permission_missing_role(self):
        data = {'permissions': ['read', 'write']}
        with self.assertRaises(ValueError) as cm:
            self.permission_service.assign_permission(data)
        self.assertIn('Missing role or permissions', str(cm.exception))

    def test_assign_permission_missing_permissions(self):
        data = {'role': 'admin'}
        with self.assertRaises(ValueError) as cm:
            self.permission_service.assign_permission(data)
        self.assertIn('Missing role or permissions', str(cm.exception))

    def test_assign_permission_empty_data(self):
        data = {}
        with self.assertRaises(ValueError) as cm:
            self.permission_service.assign_permission(data)
        self.assertIn('Missing role or permissions', str(cm.exception))

if __name__ == '__main__':
    unittest.main()