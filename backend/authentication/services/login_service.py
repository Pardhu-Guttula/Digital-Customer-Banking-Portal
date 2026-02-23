# Epic Title: User Login

import logging
from typing import Optional
from backend.authentication.models.user import User
from backend.authentication.models.login import Login

logger = logging.getLogger(__name__)

class LoginService:

    @staticmethod
    def authenticate(login: Login) -> Optional[User]:
        # Placeholder for actual authentication logic
        logger.info(f"Authenticating user with email: {login.email}")
        # Simulated authentication logic
        if login.email == "existing@user.com" and login.password == "correctpassword":
            return User(id=1, email=login.email, password=login.password)
        return None