# Epic Title: Secure and Efficient Data Storage with PostgreSQL

from typing import Optional
from backend.database.schemas.otp_schema import OtpSchema
import logging

logger = logging.getLogger(__name__)

class OtpRepository:
    def verify_otp(self, user_id: int, otp: str) -> bool:
        otp_record = OtpSchema.get_otp_by_user_id(user_id)
        if otp_record and otp_record['otp'] == otp:
            return True
        logger.warning(f"Invalid OTP for user_id {user_id}")
        return False