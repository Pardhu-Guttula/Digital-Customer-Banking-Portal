# Epic Title: Develop React UI for Submitting Service Modification Requests

import psycopg2
import logging
from backend.service_modifications.models.service_modification_request import ServiceModificationRequest

class ServiceModificationsRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def save_service_modification_request(self, request: ServiceModificationRequest):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO service_modification_requests (user_id, service_type, modification_details) 
                VALUES (%s, %s, %s)
                """, (request.user_id, request.service_type, request.modification_details))
            self.connection.commit()
            logger.info("Service modification request saved successfully")
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error saving service modification request: {e}")
            raise
        finally:
            cursor.close()