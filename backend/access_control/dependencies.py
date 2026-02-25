# Epic Title: Secure Role-Based Data Segregation in PostgreSQL

from fastapi import HTTPException, status, Depends
import logging

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    logger = logging.getLogger(__name__)
    logger.info("Validating user token")
    
    if token == "admin_token":
        return {"user_id": 1, "role": "admin"}
    elif token == "basic_token":
        return {"user_id": 2, "role": "basic"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )