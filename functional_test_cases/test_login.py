import pytest
from flask import Flask, jsonify
from flask.testing import FlaskClient

from backend.authentication.controllers.login_controller import login_bp
from backend.authentication.services.login_service import LoginService
from backend.authentication.models.login import Login

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_successful_login(client: FlaskClient):
    login_data = {"email": "existing@user.com", "password": "correctpassword"}
    response = client.post('/login', json=login_data)
    assert response.status_code == 200
    assert response.json['token'] is not None


def test_invalid_login(client: FlaskClient):
    login_data = {"email": "nonexistent@user.com", "password": "wrongpassword"}
    response = client.post('/login', json=login_data)
    assert response.status_code == 401
    assert response.json['error'] == "Invalid credentials"


def test_invalid_email_format(client: FlaskClient):
    login_data = {"email": "invalid-email-format", "password": "somepassword"}
    response = client.post('/login', json=login_data)
    assert response.status_code == 400
    assert response.json['error'] == "Invalid email format"
