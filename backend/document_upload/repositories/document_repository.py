# Epic Title: Develop Document Upload Capability Using React

import psycopg2
import logging

class DocumentRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='service_db', user='service_user', password='service_password'
        )

    def save_document_metadata(self, filename: str):
        logger = logging.getLogger(__name__)
        cursor = self.connection.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO documents (filename)
                VALUES (%s)
            """, (filename,))
            self.connection.commit()
            logger.info("Document metadata saved in PostgreSQL")
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error saving document metadata: {e}")
            raise
        finally:
            cursor.close()