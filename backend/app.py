# Epic Title: Enforce Role-Based Access Control Using FastAPI

from fastapi import FastAPI
from backend.access_control.controllers.admin_controller import router as admin_router
from backend.access_control.controllers.user_controller import router as user_router
import logging

app = FastAPI()
app.include_router(admin_router, prefix='/api')
app.include_router(user_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Role-Based Access Control Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Role-Based Access Control Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)