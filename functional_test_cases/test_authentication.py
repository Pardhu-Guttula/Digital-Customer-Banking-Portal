import pytest
from flask import Flask, jsonify
from flask.testing import FlaskClient

from backend.authentication.controllers.mfa_controller import mfa_bp
from backend.authentication.services.mfa_service import MFAService
from backend.authentication.repositories.mfa_repository import MFARepository

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(mfa_bp)
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_setup_mfa_success(client: FlaskClient, monkeypatch):
    data = {"account_id": 1, "mfa_method": "totp"}

    class MockMFAService:
        def setup_mfa(self, db, account_id, mfa_method):
            return {"success": True}

    monkeypatch.setattr(MFAService, "setup_mfa", MockMFAService().setup_mfa)
    response = client.post('/mfa/setup', json=data)
    assert response.status_code == 201
    assert response.json['success'] is True


def test_activate_mfa_success(client: FlaskClient, monkeypatch):
    data = {"account_id": 1, "mfa_method": "totp"}

    class MockMFAService:
        def activate_mfa(self, db, account_id, mfa_method):
            return {"success": True}

    monkeypatch.setattr(MFAService, "activate_mfa", MockMFAService().activate_mfa)
    response = client.post('/mfa/activate', json=data)
    assert response.status_code == 201
    assert response.json['success'] is True


def test_validate_mfa_token_success(client: FlaskClient, monkeypatch):
    data = {"account_id": 1, "token": "123456"}

    class MockMFAService:
        def validate_mfa_token(self, db, account_id, token):
            return {"success": True}

    monkeypatch.setattr(MFAService, "validate_mfa_token", MockMFAService().validate_mfa_token)
    response = client.post('/mfa/validate', json=data)
    assert response.status_code == 200
    assert response.json['success'] is True


def test_validate_mfa_token_failure(client: FlaskClient, monkeypatch):
    data = {"account_id": 1, "token": "123456"}

    class MockMFAService:
        def validate_mfa_token(self, db, account_id, token):
            return {"success": False}

    monkeypatch.setattr(MFAService, "validate_mfa_token", MockMFAService().validate_mfa_token)
    response = client.post('/mfa/validate', json=data)
    assert response.status_code == 401
    assert response.json['success'] is False
