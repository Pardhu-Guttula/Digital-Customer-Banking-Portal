# Epic Title: FastAPI Email Notification Service

import psycopg2
import logging

class EmailLogRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )
    
    def log_email_sent(self, request_id: int, status: str, user_email: str):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO email_logs (request_id, status, email)
                VALUES (%s, %s, %s)
            """, (request_id, status, user_email))
            self.connection.commit()
            logger.info(f"Logged email sent for request ID: {request_id}, status: {status}, email: {user_email}")
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error logging email: {e}")
            raise
        finally:
            cursor.close()
    
    def check_duplicate_email(self, request_id: int, status: str):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                SELECT 1 FROM email_logs 
                WHERE request_id = %s AND status = %s
            """, (request_id, status))
            result = cursor.fetchone()
            return bool(result)
        except psycopg2.Error as e:
            logger.error(f"Error checking duplicate email: {e}")
            raise
        finally:
            cursor.close()