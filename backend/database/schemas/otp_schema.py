# Epic Title: Backend User Authentication with Multi-Factor Authentication

import mysql.connector
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class OtpSchema:
    @staticmethod
    def get_otp_by_user_id(user_id: int) -> Optional[dict]:
        connection = mysql.connector.connect(host='localhost', database='user_auth', user='root', password='password')
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT * FROM otps WHERE user_id = %s", (user_id,))
            otp_data = cursor.fetchone()
            return otp_data
        except mysql.connector.Error as err:
            logger.error(f"Error fetching OTP data: {err}")
        finally:
            cursor.close()
            connection.close()
        return None