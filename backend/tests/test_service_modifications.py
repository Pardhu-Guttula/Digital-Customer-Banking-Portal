# Epic Title: Integrate PostgreSQL for Storing Service Modification Request Details

import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from backend.service_modifications.controllers.service_modifications_controller import router
from backend.service_modifications.models.service_modification_request import ServiceModificationRequest

app = FastAPI()
app.include_router(router, prefix="/api")

@pytest.mark.asyncio
async def test_valid_request():
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {
            "user_id": 1,
            "service_type": "Internet",
            "modification_details": "Upgrade to premium plan"
        }
        response = await client.post("/api/submit_modification_request", json=payload)
        assert response.status_code == 200
        assert response.json() == {"message": "Service modification request submitted successfully"}

@pytest.mark.asyncio
async def test_invalid_request():
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {
            "user_id": 1,
            "service_type": "",
            "modification_details": ""
        }
        response = await client.post("/api/submit_modification_request", json=payload)
        assert response.status_code == 400

@pytest.mark.asyncio
async def test_server_error():
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {
            "user_id": 1,
            "service_type": "Internet",
            "modification_details": "Raise server error"
        }
        response = await client.post("/api/submit_modification_request", json=payload)
        assert response.status_code == 500

@pytest.mark.asyncio
async def test_retrieve_requests():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/retrieve_modification_requests")
        assert response.status_code == 200
        assert "modifications" in response.json()