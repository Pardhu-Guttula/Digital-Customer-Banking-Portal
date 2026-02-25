# Epic Title: Integrate PostgreSQL for Storing User Credentials

from backend.authentication.repositories.auth_repository import AuthRepository
from backend.authentication.models.user import User
import logging

class AuthService:
    def __init__(self):
        self.repository = AuthRepository()

    def store_user_credentials(self, user: User):
        logger = logging.getLogger(__name__)
        logger.info(f"Storing credentials for user: {user.email}")
        self.repository.store_user_credentials(user)

    def get_user_credentials(self, email: str) -> User:
        logger = logging.getLogger(__name__)
        logger.info(f"Retrieving credentials for user: {email}")
        return self.repository.get_user_credentials(email)