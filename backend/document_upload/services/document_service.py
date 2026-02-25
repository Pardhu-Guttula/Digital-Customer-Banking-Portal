# Epic Title: Create FastAPI Endpoint to Handle Document Uploads

from backend.document_upload.repositories.document_repository import DocumentRepository
from fastapi import UploadFile
import logging
import aiofiles
import os

class DocumentService:
    def __init__(self):
        self.repository = DocumentRepository()
        self.upload_directory = "/path/to/upload/directory"
        os.makedirs(self.upload_directory, exist_ok=True)

    async def save_document(self, file: UploadFile):
        logger = logging.getLogger(__name__)
        file_location = f"{self.upload_directory}/{file.filename}"
        
        async with aiofiles.open(file_location, "wb") as buffer:
            content = await file.read()  # Read the file in bytes
            await buffer.write(content) # Write the file to destination
        
        logger.info(f"File {file.filename} saved at {file_location}")
        await self.repository.save_document_metadata(file.filename)