# Epic Title: Store Uploaded Documents in PostgreSQL

from backend.document_upload.repositories.document_repository import DocumentRepository
from fastapi import UploadFile
from cryptography.fernet import Fernet
import logging
import aiofiles
import os

class DocumentService:
    def __init__(self):
        self.repository = DocumentRepository()
        self.upload_directory = "/path/to/upload/directory"
        os.makedirs(self.upload_directory, exist_ok=True)
        self.encryption_key = Fernet.generate_key()
        self.fernet = Fernet(self.encryption_key)

    async def save_document(self, file: UploadFile):
        logger = logging.getLogger(__name__)
        encrypted_file_location = f"{self.upload_directory}/{file.filename}.enc"
        
        async with aiofiles.open(encrypted_file_location, "wb") as buffer:
            content = await file.read()
            encrypted_content = self.fernet.encrypt(content)
            await buffer.write(encrypted_content)
        
        logger.info(f"File {file.filename} saved encrypted at {encrypted_file_location}")
        await self.repository.save_document_metadata(file.filename, encrypted_file_location)