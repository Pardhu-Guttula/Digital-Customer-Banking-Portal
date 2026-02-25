# Epic Title: Implement Role-Based Access Controls for User Authorization

from fastapi import FastAPI
from backend.rbac.controllers.role_controller import router as role_router
import logging

app = FastAPI()
app.include_router(role_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Role-Based Access Control Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Role-Based Access Control Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)