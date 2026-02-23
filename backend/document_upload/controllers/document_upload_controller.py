# Epic Title: Document Upload

from flask import Blueprint, request, jsonify
from backend.document_upload.services.document_upload_service import DocumentUploadService
from backend.database.config import get_db

document_upload_bp = Blueprint('document_upload', __name__)

@document_upload_bp.route('/upload', methods=['POST'])
def upload_document():
    db = next(get_db())
    file = request.files.get('file')

    document_upload_service = DocumentUploadService(db)
    
    try:
        document_upload_service.upload_document(file)
        return jsonify({"message": "Document uploaded successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500