import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.auth_controller import auth_bp
from backend.authentication.controllers.login_controller import login_bp
from backend.authentication.controllers.mfa_controller import mfa_bp
from backend.authentication.controllers.password_recovery_controller import password_recovery_bp


@pytest.fixture(scope='module')
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(login_bp, url_prefix='/auth')
    app.register_blueprint(mfa_bp, url_prefix='/auth')
    app.register_blueprint(password_recovery_bp, url_prefix='/auth')
    return app

@pytest.fixture(scope='module')
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_login_success(client: FlaskClient):
    response = client.post('/auth/login', json={
        "email": "existing@user.com",
        "password": "correctpassword"
    })
    assert response.status_code == 200
    assert response.json["message"] == "Login successful"



def test_login_failure(client: FlaskClient):
    response = client.post('/auth/login', json={
        "email": "nonexistent@user.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json["error"] == "Invalid credentials"


def test_validate_mfa_token_success(client: FlaskClient):
    response = client.post('/auth/mfa/validate', json={
        "account_id": 1,
        "token": "correcttoken"
    })
    assert response.status_code == 200
    assert response.json["success"] is True


def test_validate_mfa_token_failure(client: FlaskClient):
    response = client.post('/auth/mfa/validate', json={
        "account_id": 1,
        "token": "wrongtoken"
    })
    assert response.status_code == 401
    assert response.json["success"] is False


def test_setup_mfa_success(client: FlaskClient):
    response = client.post('/auth/mfa/setup', json={
        "account_id": 1,
        "mfa_method": "email"
    })
    assert response.status_code == 201
    assert response.json["success"] is True


def test_setup_mfa_failure(client: FlaskClient):
    response = client.post('/auth/mfa/setup', json={
        "account_id": 1,
        "mfa_method": "invalid_method"
    })
    assert response.status_code == 500
    assert response.json["error"] == "Unable to process your request"


def test_activate_mfa_success(client: FlaskClient):
    response = client.post('/auth/mfa/activate', json={
        "account_id": 1,
        "mfa_method": "email"
    })
    assert response.status_code == 201
    assert response.json["success"] is True


def test_activate_mfa_failure(client: FlaskClient):
    response = client.post('/auth/mfa/activate', json={
        "account_id": 1,
        "mfa_method": "invalid_method"
    })
    assert response.status_code == 500
    assert response.json["error"] == "Unable to process your request"


def test_password_recovery_success(client: FlaskClient):
    response = client.post('/auth/password-recovery', json={
       "email": "existing@user.com"
    })
    assert response.status_code == 200
    assert response.json["message"] == "Password recovery email sent"


def test_password_recovery_failure(client: FlaskClient):
    response = client.post('/auth/password-recovery', json={
       "email": "nonexistent@user.com"
    })
    assert response.status_code == 400
    assert response.json["error"] == "Email not recognized"


def test_password_recovery_validation_error(client: FlaskClient):
    response = client.post('/auth/password-recovery', json={
       "email": ""
    })
    assert response.status_code == 400
    assert "errors" in response.json
