# Epic Title: Secure and Efficient Data Storage with PostgreSQL

import psycopg2
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class OtpSchema:
    @staticmethod
    def get_otp_by_user_id(user_id: int) -> Optional[dict]:
        connection = psycopg2.connect(
            host='localhost', database='auth_db', user='auth_user', password='auth_password'
        )
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM otps WHERE user_id = %s", (user_id,))
            otp_data = cursor.fetchone()
            if otp_data:
                return {'user_id': otp_data[0], 'otp': otp_data[1]}
        except psycopg2.Error as e:
            logger.error(f"Error fetching OTP data: {e}")
        finally:
            cursor.close()
            connection.close()
        return None