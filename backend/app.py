# Epic Title: FastAPI Backend for Service Modification Requests

from fastapi import FastAPI
from backend.service_modifications.controllers.service_modification_controller import router as service_modification_router
import logging

app = FastAPI()
app.include_router(service_modification_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Service Modification System"}

if __name__ == '__main__':
    logger.info("Starting the Service Modification System...")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)