# Epic Title: FastAPI Email Notification Service

from fastapi import FastAPI
from backend.email_notifications.controllers.email_notification_controller import router as email_notification_router
import logging

app = FastAPI()
app.include_router(email_notification_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Email Notification Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Email Notification Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)