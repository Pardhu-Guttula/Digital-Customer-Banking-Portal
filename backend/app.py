# Epic Title: Backend Process Workflows for Account Opening

from fastapi import FastAPI
from backend.application.controllers.account_opening_controller import router as account_opening_router
import logging

app = FastAPI()
app.include_router(account_opening_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Backend Process Workflows"}

if __name__ == '__main__':
    logger.info("Starting the Backend Process Workflows System...")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)