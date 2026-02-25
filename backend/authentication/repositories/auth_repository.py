# Epic Title: Develop Secure Authentication Mechanisms Using FastAPI

import psycopg2
import logging
from backend.authentication.models.user import User
from backend.authentication.models.otp import OTP

class AuthRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def get_user_by_email(self, email: str) -> User:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT email, password_hash FROM users WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                return User(email=result[0], password_hash=result[1])
            return None
        except psycopg2.Error as e:
            logger.error(f"Error fetching user by email: {e}")
            raise
        finally:
            cursor.close()

    def get_otp_by_email(self, email: str) -> OTP:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT email, otp FROM otps WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                return OTP(email=result[0], otp=result[1])
            return None
        except psycopg2.Error as e:
            logger.error(f"Error fetching OTP by email: {e}")
            raise
        finally:
            cursor.close()

    def invalidate_otp(self, email: str):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM otps WHERE email = %s", (email,))
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error invalidating OTP: {e}")
            raise
        finally:
            cursor.close()

    def create_user(self, email: str, hashed_password: str):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO users (email, password_hash) VALUES (%s, %s)", (email, hashed_password))
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error creating user: {e}")
            raise
        finally:
            cursor.close()