import pytest
import json
from fastapi.testclient import TestClient
from backend.authentication.controllers.auth_controller import router
from backend.authentication.controllers.login_controller import login_controller
from backend.authentication.controllers.mfa_controller import mfa_bp
from backend.authentication.models.user import User
from backend.authentication.repositories.mfa_repository import MFARepository
from backend.authentication.services.mfa_service import MFAService
from backend.database.config import get_db

client = TestClient(router)


@pytest.fixture
async def user_data():
    return {
        "email": "user@example.com",
        "password": "securepassword"
    }


@pytest.mark.asyncio
async def test_successful_login(user_data):
    response = await client.post("/login", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })

    assert response.status_code == 200
    assert "token" in response.json()


@pytest.mark.asyncio
async def test_invalid_credentials(user_data):
    response = await client.post("/login", json={
        "email": user_data["email"],
        "password": "wrongpassword"
    })

    assert response.status_code == 401
    assert response.json() == {"error": "Invalid credentials"}


@pytest.mark.asyncio
async def test_form_validation():
    response = await client.post("/login", json={
        "email": "invalidemail"
    })

    assert response.status_code == 400
    assert response.json() == {"error": "Email and password are required"}


client = TestClient(login_controller)


@pytest.mark.asyncio
async def test_setup_mfa():
    data = {
        "account_id": "123",
        "mfa_method": "totp"
    }

    response = await client.post("/mfa/setup", json=data)
    assert response.status_code == 201
    result = response.json()
    assert result.get("success") is True


@pytest.mark.asyncio
async def test_setup_mfa_failure():
    data = {
        "account_id": None,
        "mfa_method": "totp"
    }

    response = await client.post("/mfa/setup", json=data)
    assert response.status_code == 500
    result = response.json()
    assert result.get("error") == "Unable to process your request"


@pytest.mark.asyncio
async def test_activate_mfa():
    data = {
        "account_id": "123",
        "mfa_method": "totp"
    }

    response = await client.post("/mfa/activate", json=data)
    assert response.status_code == 201
    result = response.json()
    assert result.get("success") is True


@pytest.mark.asyncio
async def test_activate_mfa_failure():
    data = {
        "account_id": "123",
        "mfa_method": "sms"
    }

    response = await client.post("/mfa/activate", json=data)
    assert response.status_code == 500
    result = response.json()
    assert result.get("error") == "Unable to process your request"


client = TestClient(mfa_bp)


@pytest.mark.asyncio
async def test_validate_mfa_token():
    data = {
        "account_id": "123",
        "token": "654321"
    }

    response = await client.post("/mfa/validate", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result.get("success") is True


@pytest.mark.asyncio
async def test_validate_mfa_token_failure():
    data = {
        "account_id": "123",
        "token": "123456"
    }

    response = await client.post("/mfa/validate", json=data)
    assert response.status_code == 401
    result = response.json()
    assert result.get("success") is False
