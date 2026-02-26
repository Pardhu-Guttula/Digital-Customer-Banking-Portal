# File: tests/test_account_repository.py

import pytest
from unittest.mock import MagicMock

from your_module import AccountRepository


@pytest.fixture
def db_session():
    return MagicMock()


@pytest.fixture
def repository(db_session):
    return AccountRepository(db_session)


def test_save_account_opening_request_success(repository, db_session):
    data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '1234567890',
        'address': '123 Main St',
        'income': 50000
    }
    
    repository.save_account_opening_request(data)
    
    db_session.execute.assert_called_once()
    db_session.commit.assert_called_once()


def test_save_account_opening_request_missing_required_fields(repository, db_session):
    data = {}
    
    with pytest.raises(KeyError):
        repository.save_account_opening_request(data)
    
    db_session.execute.assert_not_called()
    db_session.commit.assert_not_called()


def test_save_account_opening_request_null_data(repository, db_session):
    data = None
    
    with pytest.raises(TypeError):
        repository.save_account_opening_request(data)
    
    db_session.execute.assert_not_called()
    db_session.commit.assert_not_called()


def test_save_account_opening_request_partial_data(repository, db_session):
    data = {
        'name': 'John Doe',
        'income': 50000
    }
    
    with pytest.raises(KeyError):
        repository.save_account_opening_request(data)
    
    db_session.execute.assert_not_called()
    db_session.commit.assert_not_called()


def test_save_account_opening_request_sql_failure(repository, db_session):
    data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '1234567890',
        'address': '123 Main St',
        'income': 50000
    }
    
    db_session.execute.side_effect = Exception('SQL Error')
    
    with pytest.raises(Exception, match='SQL Error'):
        repository.save_account_opening_request(data)
    
    db_session.commit.assert_not_called()