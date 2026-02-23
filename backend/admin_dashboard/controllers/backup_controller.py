# Epic Title: Integrate with PostgreSQL for Data Storage

import logging
from fastapi import APIRouter
from subprocess import call

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/backup", status_code=200)
def create_backup():
    try:
        call(["pg_dump", "-U", "user", "-h", "localhost", "mydatabase", "-F", "c", "-b", "-v", "-f", "backup.dump"])
        logger.info("Database backup created successfully")
        return {"message": "Backup created successfully"}
    except Exception as e:
        logger.error(f"Error creating backup: {str(e)}")
        return {"error": f"Error creating backup: {str(e)}"}, 500