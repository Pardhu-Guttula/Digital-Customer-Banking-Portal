# Epic Title: Develop Secure Authentication Mechanisms Using FastAPI

from fastapi import HTTPException, status, Depends
import jwt
import logging

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    logger = logging.getLogger(__name__)
    logger.info("Validating user token")
    secret_key = "your-secret-key"
    
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        email = payload.get("email")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )
        return {"email": email}
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )