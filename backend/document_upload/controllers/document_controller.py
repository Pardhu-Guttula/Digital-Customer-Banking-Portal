# Epic Title: Store Uploaded Documents in PostgreSQL

from fastapi import APIRouter, UploadFile, File, HTTPException, status
from backend.document_upload.services.document_service import DocumentService
import logging

router = APIRouter()
service = DocumentService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    logger.info("Received document to upload")

    # Validate file type
    allowed_file_types = ["application/pdf", "image/jpeg", "image/png"]
    if file.content_type not in allowed_file_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")

    try:
        await service.save_document(file)
        return {"message": "Document uploaded successfully"}
    except Exception as e:
        logger.error(f"Error uploading document: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")