# Epic Title: Resume Incomplete Applications

import psycopg2
import logging

class ApplicationRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def save_application(self, data: dict):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO applications (user_id, application_data)
                VALUES (%s, %s)
                ON CONFLICT (user_id) DO UPDATE 
                SET application_data = EXCLUDED.application_data
            """, (data['user_id'], data['application_data']))
            self.connection.commit()
            logger.info("Application data saved in PostgreSQL")
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error saving application data: {e}")
            raise
        finally:
            cursor.close()

    def get_application(self, user_id: int) -> dict:
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                SELECT application_data
                FROM applications
                WHERE user_id = %s
            """, (user_id,))
            result = cursor.fetchone()
            if result:
                return {
                    "user_id": user_id,
                    "application_data": result[0]
                }
            return None
        except psycopg2.Error as e:
            logger.error(f"Error retrieving application data: {e}")
            raise
        finally:
            cursor.close()