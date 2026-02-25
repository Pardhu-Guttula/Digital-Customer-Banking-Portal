# Epic Title: Integrate PostgreSQL for Storing User Credentials

import psycopg2
import logging
from backend.authentication.models.user import User
from cryptography.fernet import Fernet

class AuthRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )
        self.encryption_key = Fernet.generate_key()
        self.fernet = Fernet(self.encryption_key)

    def store_user_credentials(self, user: User):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            encrypted_password = self.fernet.encrypt(user.password.encode())
            cursor.execute("INSERT INTO users (email, password_hash) VALUES (%s, %s)",
                           (user.email, encrypted_password))
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error storing user credentials: {e}")
            raise
        finally:
            cursor.close()

    def get_user_credentials(self, email: str) -> User:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT email, password_hash FROM users WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                decrypted_password = self.fernet.decrypt(result[1]).decode()
                return User(email=result[0], password=decrypted_password)
            return None
        except psycopg2.Error as e:
            logger.error(f"Error retrieving user credentials: {e}")
            raise
        finally:
            cursor.close()