# Epic Title: Create FastAPI Endpoint to Handle Document Uploads

import asyncpg
import logging

class DocumentRepository:
    def __init__(self):
        self.dsn = 'postgresql://service_user:service_password@localhost:5432/service_db'

    async def save_document_metadata(self, filename: str):
        conn = await asyncpg.connect(dsn=self.dsn)
        logger = logging.getLogger(__name__)
        
        try:
            await conn.execute("""
                INSERT INTO documents (filename)
                VALUES ($1)
            """, filename)
            logger.info("Document metadata saved in PostgreSQL")
        except Exception as e:
            logger.error(f"Error saving document metadata: {e}")
            raise
        finally:
            await conn.close()