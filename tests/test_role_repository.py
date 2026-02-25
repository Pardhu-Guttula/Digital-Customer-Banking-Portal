# File: tests/test_role_repository.py

import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from role_repository import RoleRepository

class TestRoleRepository(unittest.TestCase):

    def setUp(self):
        self.db_session = MagicMock(spec=Session)
        self.role_repository = RoleRepository(self.db_session)

    def test_create_role_success(self):
        self.db_session.execute.return_value = None
        self.db_session.commit.return_value = None
        self.role_repository.create_role('admin')
        self.db_session.execute.assert_called_once_with("INSERT INTO roles (name) VALUES (:role_name)", {'role_name': 'admin'})
        self.db_session.commit.assert_called_once()

    def test_create_role_with_empty_name(self):
        self.db_session.execute.return_value = None
        self.db_session.commit.return_value = None
        self.role_repository.create_role('')
        self.db_session.execute.assert_called_once_with("INSERT INTO roles (name) VALUES (:role_name)", {'role_name': ''})
        self.db_session.commit.assert_called_once()

    def test_get_roles_success(self):
        self.db_session.execute.return_value.fetchall.return_value = [{'id': 1, 'name': 'admin'}, {'id': 2, 'name': 'user'}]
        roles = self.role_repository.get_roles()
        self.db_session.execute.assert_called_once_with("SELECT * FROM roles")
        self.assertEqual(roles, [{'id': 1, 'name': 'admin'}, {'id': 2, 'name': 'user'}])

    def test_get_roles_empty(self):
        self.db_session.execute.return_value.fetchall.return_value = []
        roles = self.role_repository.get_roles()
        self.db_session.execute.assert_called_once_with("SELECT * FROM roles")
        self.assertEqual(roles, [])

    def test_create_role_exception(self):
        self.db_session.execute.side_effect = Exception('Database error')
        with self.assertRaises(Exception) as context:
            self.role_repository.create_role('admin')
        self.assertTrue('Database error' in str(context.exception))

    def test_get_roles_exception(self):
        self.db_session.execute.side_effect = Exception('Database error')
        with self.assertRaises(Exception) as context:
            self.role_repository.get_roles()
        self.assertTrue('Database error' in str(context.exception))

if __name__ == '__main__':
    unittest.main()