# Epic Title: Develop Secure Authentication Mechanisms Using FastAPI

from fastapi import APIRouter, Depends, HTTPException, status
from backend.authentication.services.auth_service import AuthService
from backend.authentication.models.user import User
from backend.authentication.dependencies import get_current_user
import logging

router = APIRouter()
service = AuthService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/login")
async def login(user: User):
    logger.info(f"User attempting to login: {user.email}")
    try:
        token = service.login(user)
        return {"message": "Login successful", "token": token}
    except ValueError as e:
        logger.error(f"Login failed: {e}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

@router.post("/verify-otp")
async def verify_otp(otp: str, current_user: dict = Depends(get_current_user)):
    logger.info(f"User {current_user['email']} attempting to verify OTP")
    try:
        service.verify_otp(current_user['email'], otp)
        return {"message": "OTP verification successful"}
    except ValueError as e:
        logger.error(f"OTP verification failed: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))