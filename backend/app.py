# Epic Title: Integrate PostgreSQL for Storing User Credentials

from fastapi import FastAPI
from backend.authentication.controllers.auth_controller import router as auth_router
import logging

app = FastAPI()
app.include_router(auth_router, prefix='/api')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Authentication Service"}

if __name__ == '__main__':
    import uvicorn
    logger.info("Starting the Authentication Service...")
    uvicorn.run(app, host='0.0.0.0', port=8000)