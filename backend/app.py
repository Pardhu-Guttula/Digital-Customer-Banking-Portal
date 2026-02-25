# Epic Title: Develop Document Upload Capability Using React

from fastapi import FastAPI
from backend.document_upload.controllers.document_controller import router as document_router
import logging

app = FastAPI()
app.include_router(document_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Document Upload Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Document Upload Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)