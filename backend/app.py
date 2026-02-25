# Epic Title: Resume Incomplete Applications

from fastapi import FastAPI
from backend.incomplete_applications.controllers.application_controller import router as application_router
import logging

app = FastAPI()
app.include_router(application_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Incomplete Application Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Incomplete Application Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)