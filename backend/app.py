# Epic Title: Integrate Self-Service Portal with Core Banking System

from fastapi import FastAPI
from backend.integration.core_banking.controllers.integration_controller import router as integration_router
import logging

app = FastAPI()
app.include_router(integration_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Integration Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Integration Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)