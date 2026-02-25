# Epic Title: Develop Document Upload Capability Using React

from backend.document_upload.repositories.document_repository import DocumentRepository
from fastapi import UploadFile
import logging
import shutil
import os

class DocumentService:
    def __init__(self):
        self.repository = DocumentRepository()
        self.upload_directory = "/path/to/upload/directory"
        os.makedirs(self.upload_directory, exist_ok=True)

    def save_document(self, file: UploadFile):
        logger = logging.getLogger(__name__)
        file_location = f"{self.upload_directory}/{file.filename}"
        
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        logger.info(f"File {file.filename} saved at {file_location}")
        self.repository.save_document_metadata(file.filename)