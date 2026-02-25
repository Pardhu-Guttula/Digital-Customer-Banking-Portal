# Epic Title: Real-time Status Updates Using React and Redis

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

    def update_status(self, request_id: int, status: str):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO status_updates (request_id, status)
                VALUES (%s, %s)
                ON CONFLICT (request_id) DO UPDATE SET status = %s
            """, (request_id, status, status))
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error updating status in database: {e}")
            raise
        finally:
            cursor.close()