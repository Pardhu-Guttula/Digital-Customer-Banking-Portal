# Epic Title: Login and Authentication

from fastapi import APIRouter, HTTPException, status
from backend.authentication.services.auth_service import AuthService
from backend.authentication.models.user import User
import logging

router = APIRouter()
service = AuthService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/store")
async def store_user(user: User):
    logger.info(f"Storing user credentials: {user.email}")
    try:
        service.store_user_credentials(user)
        return {"message": "User credentials stored successfully"}
    except Exception as e:
        logger.error(f"Error storing user credentials: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.get("/retrieve")
async def retrieve_user(email: str):
    logger.info(f"Retrieving user credentials for email: {email}")
    try:
        user = service.get_user_credentials(email)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return {"email": user.email, "password": user.password}
    except Exception as e:
        logger.error(f"Error retrieving user credentials: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
