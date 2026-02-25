# Epic Title: Secure and Efficient Data Storage with PostgreSQL

import psycopg2
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
import logging

logger = logging.getLogger(__name__)

class UserSchema:
    @staticmethod
    def get_user_by_email(email: str) -> Optional[dict]:
        connection = psycopg2.connect(
            host='localhost', database='auth_db', user='auth_user', password='auth_password'
        )
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user_record = cursor.fetchone()
            if user_record:
                user = {
                    'id': user_record[0],
                    'email': user_record[1],
                    'password_hash': user_record[2]
                }
                return user
        except psycopg2.Error as e:
            logger.error(f"Error fetching user by email: {e}")
        finally:
            cursor.close()
            connection.close()
        return None

    @staticmethod
    def store_user(email: str, password: str):
        connection = psycopg2.connect(
            host='localhost', database='auth_db', user='auth_user', password='auth_password'
        )
        cursor = connection.cursor()

        try:
            password_hash = generate_password_hash(password)
            cursor.execute(
                "INSERT INTO users (email, password_hash) VALUES (%s, %s)",
                (email, password_hash)
            )
            connection.commit()
        except psycopg2.Error as e:
            logger.error(f"Error storing user: {e}")
        finally:
            cursor.close()
            connection.close()