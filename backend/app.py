# Epic Title: Secure Role-Based Data Segregation in PostgreSQL

from fastapi import FastAPI
from backend.rbac.controllers.data_controller import router as data_router
import logging

app = FastAPI()
app.include_router(data_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Secure Role-Based Data Segregation Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Secure Role-Based Data Segregation Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)