# Epic Title: Document Upload

import os
from werkzeug.utils import secure_filename
from backend.document_upload.repositories.document_repository import DocumentRepository

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'jpg', 'png'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

class DocumentUploadService:
    def __init__(self, db):
        self.document_repository = DocumentRepository(db)

    def upload_document(self, file):
        if not file or not self.allowed_file(file.filename):
            raise ValueError('Invalid file type')
        
        if file.content_length > MAX_FILE_SIZE:
            raise ValueError('File size exceeds the maximum limit')

        filename = secure_filename(file.filename)
        file_path = os.path.join('/path/to/upload/directory', filename)
        
        file.save(file_path)

        self.document_repository.save_document({
            'filename': filename,
            'path': file_path
        })

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS