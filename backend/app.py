# Epic Title: Secure and Efficient Data Storage with PostgreSQL

from fastapi import FastAPI
from backend.authentication.controllers.auth_controller import router as auth_router
import logging

app = FastAPI()
app.include_router(auth_router, prefix='/auth')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
async def home():
    return {"message": "Welcome to the Secure User Authentication System"}

if __name__ == '__main__':
    logger.info("Starting the User Authentication System with Secure Data Storage...")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)