# Epic Title: Personalized User Dashboard in React

import psycopg2
import logging

class UserRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def get_user_profile(self, email: str) -> dict:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, name, email, eligibility FROM users WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                return {
                    "id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "eligibility": result[3]
                }
            return {}
        except psycopg2.Error as e:
            logger.error(f"Error fetching user profile: {e}")
            raise
        finally:
            cursor.close()