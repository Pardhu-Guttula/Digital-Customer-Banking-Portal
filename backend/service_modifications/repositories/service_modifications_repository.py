# Epic Title: Integrate PostgreSQL for Storing Service Modification Request Details

import psycopg2
import logging
from backend.service_modifications.models.service_modification_request import ServiceModificationRequest, Field

class ServiceModificationsRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def save_modification_request(self, request: ServiceModificationRequest):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO service_modification_requests (user_id, service_type, modification_details, status) 
                VALUES (%s, %s, %s, %s)
                """, (request.user_id, request.service_type, request.modification_details, request.status))
            self.connection.commit()
            logger.info("Service modification request saved successfully")
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error saving modification request: {e}")
            raise
        finally:
            cursor.close()

    def retrieve_modification_requests(self):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM service_modification_requests")
            result = cursor.fetchall()
            logger.info("Retrieved modification requests successfully")
            return result
        except psycopg2.Error as e:
            logger.error(f"Error retrieving modification requests: {e}")
            raise
        finally:
            cursor.close()