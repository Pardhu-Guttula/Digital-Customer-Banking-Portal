# Epic Title: Backend API Development with FastAPI

import psycopg2
import logging

class StatusUpdateRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def fetch_status(self, request_id: int):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT status FROM status_updates WHERE request_id = %s", (request_id,))
            row = cursor.fetchone()
            if row:
                return row[0]
            return None
        except psycopg2.Error as e:
            logger.error(f"Error fetching status from database: {e}")
            raise
        finally:
            cursor.close()