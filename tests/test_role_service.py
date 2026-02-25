# File: tests/test_role_service.py

import unittest
from unittest.mock import MagicMock
from backend.access_control.repositories.role_repository import RoleRepository
from backend.access_control.services.role_service import RoleService

class TestRoleService(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.role_repository_mock = MagicMock(spec=RoleRepository)
        self.role_service = RoleService(self.db_mock)
        self.role_service.role_repository = self.role_repository_mock

    def test_create_role_success(self):
        data = {'role_name': 'admin'}
        self.role_service.create_role(data)
        self.role_repository_mock.create_role.assert_called_once_with('admin')

    def test_create_role_missing_role_name(self):
        data = {}
        with self.assertRaises(ValueError) as context:
            self.role_service.create_role(data)
        self.assertEqual(str(context.exception), 'Missing role name')
        self.role_repository_mock.create_role.assert_not_called()

    def test_get_roles_success(self):
        self.role_repository_mock.get_roles.return_value = ['admin', 'user']
        roles = self.role_service.get_roles()
        self.assertEqual(roles, ['admin', 'user'])
        self.role_repository_mock.get_roles.assert_called_once()

if __name__ == '__main__':
    unittest.main()