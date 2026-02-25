# File: tests/test_user_service.py

import pytest
from unittest.mock import Mock, create_autospec
from backend.access_control.services.user_service import UserService
from backend.access_control.repositories.user_repository import UserRepository

@pytest.fixture
def user_service():
    db = Mock()
    return UserService(db)

@pytest.fixture
def mock_user_repository():
    return create_autospec(UserRepository)

@pytest.fixture
def user_service_with_mock_repo(mock_user_repository):
    service = UserService(None)
    service.user_repository = mock_user_repository
    return service

class TestUserService:
    def test_assign_role_success(self, user_service_with_mock_repo, mock_user_repository):
        user_id = "user-123"
        data = {"role": "admin"}

        user_service_with_mock_repo.assign_role(user_id, data)

        mock_user_repository.assign_role.assert_called_once_with(user_id, "admin")
    
    def test_assign_role_missing_role(self, user_service_with_mock_repo):
        user_id = "user-123"
        data = {}

        with pytest.raises(ValueError, match="Missing role"):
            user_service_with_mock_repo.assign_role(user_id, data)

    def test_get_user_permissions_success(self, user_service_with_mock_repo, mock_user_repository):
        user_id = "user-123"
        expected_permissions = ["read", "write"]
        mock_user_repository.get_user_permissions.return_value = expected_permissions

        result = user_service_with_mock_repo.get_user_permissions(user_id)

        assert result == expected_permissions
        mock_user_repository.get_user_permissions.assert_called_once_with(user_id)

    def test_get_user_permissions_no_permissions(self, user_service_with_mock_repo, mock_user_repository):
        user_id = "user-123"
        mock_user_repository.get_user_permissions.return_value = []

        result = user_service_with_mock_repo.get_user_permissions(user_id)

        assert result == []
        mock_user_repository.get_user_permissions.assert_called_once_with(user_id)

    def test_assign_role_with_invalid_user_id(self, user_service_with_mock_repo, mock_user_repository):
        user_id = None
        data = {"role": "admin"}

        with pytest.raises(TypeError):
            user_service_with_mock_repo.assign_role(user_id, data)

    def test_assign_role_with_invalid_role_type(self, user_service_with_mock_repo, mock_user_repository):
        user_id = "user-123"
        data = {"role": 123}

        with pytest.raises(TypeError):
            user_service_with_mock_repo.assign_role(user_id, data)

    def test_get_user_permissions_with_invalid_user_id(self, user_service_with_mock_repo, mock_user_repository):
        user_id = None

        with pytest.raises(TypeError):
            user_service_with_mock_repo.get_user_permissions(user_id)
