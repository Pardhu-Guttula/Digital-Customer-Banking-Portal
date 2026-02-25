# Epic Title: Log Email Communication in PostgreSQL

from fastapi import APIRouter, HTTPException
from backend.email_notifications.services.email_service import EmailNotificationService
import logging

router = APIRouter()
service = EmailNotificationService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/send_email")
async def send_email_notification(request_id: int, status: str, user_email: str):
    logger.info(f"Sending email notification for request ID: {request_id} with status: {status} to user {user_email}")
    try:
        result = service.send_email(request_id, status, user_email)
        if not result:
            raise HTTPException(status_code=500, detail="Failed to send email")
        return {"message": "Email sent successfully"}
    except HTTPException as e:
        logger.error(f"HTTP error: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Internal server error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")