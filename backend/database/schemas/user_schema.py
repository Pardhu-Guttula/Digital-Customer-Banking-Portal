# Epic Title: Backend User Authentication with Multi-Factor Authentication

import mysql.connector
import logging

logger = logging.getLogger(__name__)

class UserSchema:
    @staticmethod
    def get_user_by_email(email: str) -> Optional[dict]:
        connection = mysql.connector.connect(host='localhost', database='user_auth', user='root', password='password')
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user_data = cursor.fetchone()
            return user_data
        except mysql.connector.Error as err:
            logger.error(f"Error fetching user data: {err}")
        finally:
            cursor.close()
            connection.close()
        return None