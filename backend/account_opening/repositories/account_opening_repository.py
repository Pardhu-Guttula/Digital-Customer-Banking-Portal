# Epic Title: PostgreSQL Data Storage for Account Opening Requests

import psycopg2
import logging

class AccountOpeningRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='bank_system', user='bank_user', password='bank_password'
        )

    def store_request(self, data: dict):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO account_opening_requests (name, email, phone, address)
                VALUES (%s, %s, %s, %s)
            """, (data['name'], data['email'], data['phone'], data['address']))
            self.connection.commit()
            logger.info("Account opening request stored in PostgreSQL")
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error storing account opening request: {e}")
            raise
        finally:
            cursor.close()