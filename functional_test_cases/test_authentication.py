import pytest
from flask import json
from backend.authentication.controllers.auth_controller import auth_bp
from backend.authentication.controllers.login_controller import login_bp
from backend.authentication.controllers.mfa_controller import mfa_bp
from backend.authentication.controllers.password_recovery_controller import password_recovery_bp
from backend.database.config import get_db

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def app():
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(mfa_bp)
    app.register_blueprint(password_recovery_bp)
    return app

# Tests for login functionality
def test_login_success(client):
    response = client.post('/login', json={"email": "existing@user.com", "password": "correctpassword"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "message" in data
    assert data["message"] == "Login successful"

def test_login_invalid_credentials(client):
    response = client.post('/login', json={"email": "wrong@user.com", "password": "wrongpassword"})
    data = json.loads(response.data)
    assert response.status_code == 401
    assert "error" in data
    assert data["error"] == "Invalid credentials"

def test_login_validation_error(client):
    response = client.post('/login', json={"email": "existing@user.com"})
    data = json.loads(response.data)
    assert response.status_code == 400
    assert "errors" in data

# Tests for MFA token validation
def test_validate_mfa_token_success(client):
    response = client.post('/mfa/validate', json={"account_id": 1, "token": "123456"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "success" in data
    assert data["success"] is True

def test_validate_mfa_token_failure(client):
    response = client.post('/mfa/validate', json={"account_id": 1, "token": "wrongtoken"})
    data = json.loads(response.data)
    assert response.status_code == 401
    assert "success" in data
    assert data["success"] is False

# Tests for Password Recovery
def test_password_recovery_success(client):
    response = client.post('/password-recovery', json={"email": "existing@user.com"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "message" in data
    assert data["message"] == "Password recovery email sent"

def test_password_recovery_invalid_email(client):
    response = client.post('/password-recovery', json={"email": "notfound@user.com"})
    data = json.loads(response.data)
    assert response.status_code == 400
    assert "error" in data
    assert data["error"] == "Email not recognized"
