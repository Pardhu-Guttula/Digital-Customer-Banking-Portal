# Epic Title: Backend API Development with FastAPI

from fastapi import FastAPI
from backend.realtime_status_updates.controllers.status_update_controller import router as status_update_router
import logging

app = FastAPI()
app.include_router(status_update_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Real-time Status Update System"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Real-time Status Update System...")
    uvicorn.run(app, host='0.0.0.0', port=8000)