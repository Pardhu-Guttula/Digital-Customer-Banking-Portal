# Epic Title: Redis Caching for Service Modification Workflows

import psycopg2
import logging

class ServiceModificationRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def store_request(self, data: dict):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO service_modifications (service_name, modification_details)
                VALUES (%s, %s)
            """, (data['service_name'], data['modification_details']))
            self.connection.commit()
            logger.info("Service modification request stored in PostgreSQL")
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error storing service modification request: {e}")
            raise
        finally:
            cursor.close()

    def retrieve_all_requests(self):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()

        try:
            cursor.execute("""
                SELECT service_name, modification_details
                FROM service_modifications
            """)
            rows = cursor.fetchall()
            self.connection.commit()
            logger.info("Service modification requests retrieved")
            return [{"service_name": row[0], "modification_details": row[1]} for row in rows]
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error retrieving service modification requests: {e}")
            raise
        finally:
            cursor.close()