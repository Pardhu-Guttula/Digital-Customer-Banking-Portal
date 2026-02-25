# File: tests/test_permission_repository.py
import pytest
from sqlalchemy.orm import Session
from unittest import mock
from your_module import PermissionRepository

@pytest.fixture
@mock.patch('your_module.Session')
def db_session_mock(Session):
    session = mock.Mock(spec=Session)
    yield session

class TestPermissionRepository:

    # Test assigning permissions to a role (positive scenario)
    def test_assign_permission_success(self, db_session_mock):
        repository = PermissionRepository(db_session_mock)
        db_session_mock.execute.side_effect = [
            {'fetchone.return_value': {'id': 1}},  # Mock role_id fetching
            True,  # For inserting each permission
        ]

        repository.assign_permission('admin', ['read', 'write', 'delete'])

        assert db_session_mock.execute.call_count == 4  # 1 for fetching role_id + 3 for each permission
        db_session_mock.commit.assert_called_once()

    # Test assigning permission with empty permission list
    def test_assign_permission_empty_list(self, db_session_mock):
        repository = PermissionRepository(db_session_mock)
        db_session_mock.execute.return_value.fetchone.return_value = {'id': 1}

        repository.assign_permission('admin', [])

        db_session_mock.execute.assert_called_once()  # Only role_id fetching is called
        db_session_mock.commit.assert_called_once()

    # Test assigning permission to non-existent role (negative scenario)
    def test_assign_permission_role_not_found(self, db_session_mock):
        repository = PermissionRepository(db_session_mock)
        db_session_mock.execute.return_value.fetchone.return_value = None

        with pytest.raises(KeyError):  # Assuming KeyError for missing role_id
            repository.assign_permission('non_existent_role', ['read'])

        db_session_mock.commit.assert_not_called()

    # Test exception during permission assignment
    def test_assign_permission_exception(self, db_session_mock):
        repository = PermissionRepository(db_session_mock)
        db_session_mock.execute.side_effect = Exception('DB Error')

        with pytest.raises(Exception, match='DB Error'):
            repository.assign_permission('admin', ['read'])

        db_session_mock.commit.assert_not_called()

    # Test handling null session
    def test_assign_permission_null_session(self):
        with pytest.raises(TypeError):
            PermissionRepository(None)
