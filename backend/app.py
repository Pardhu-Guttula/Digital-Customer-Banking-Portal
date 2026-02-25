# Epic Title: Implement FastAPI Backend for Handling Service Modification Requests

from fastapi import FastAPI
from backend.service_modifications.controllers.service_modifications_controller import router as service_modifications_router
import logging

app = FastAPI()
app.include_router(service_modifications_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Service Modifications Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Service Modifications Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)