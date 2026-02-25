# Epic Title: Backend User Authentication with Multi-Factor Authentication

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from backend.authentication.services.auth_service import AuthService
from backend.authentication.models.user import User
import logging

router = APIRouter()
auth_service = AuthService()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class AuthRequest(BaseModel):
    email: str
    password: str
    otp: str

@router.post('/authenticate')
async def authenticate(auth_request: AuthRequest):
    logger.info("Authentication attempt with provided credentials.")
    user = auth_service.authenticate(auth_request.email, auth_request.password, auth_request.otp)
    if user:
        token = auth_service.generate_session_token(user)
        logger.info(f"User {auth_request.email} authenticated successfully.")
        return {"message": "Authentication successful", "token": token}
    else:
        logger.warning(f"Invalid authentication attempt for email {auth_request.email}.")
        raise HTTPException(status_code=401, detail="Invalid credentials or OTP")