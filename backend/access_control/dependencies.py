# Epic Title: Enforce Role-Based Access Control Using FastAPI

from fastapi import HTTPException, status, Depends
import logging

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    # This is a placeholder function. Implement actual token parsing and user retrieval logic
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