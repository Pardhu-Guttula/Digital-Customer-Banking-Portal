# Epic Title: Store User Interaction Data in PostgreSQL

from backend.interaction_history.repositories.interaction_repository import InteractionRepository
import logging

class InteractionService:
    def __init__(self):
        self.repository = InteractionRepository()

    def store_interaction(self, data: dict):
        logger = logging.getLogger(__name__)
        logger.info("Storing interaction data")

        # Validate data integrity
        if not self.validate_data(data):
            logger.error("Data integrity validation failed")
            raise ValueError("Invalid interaction data")

        # Store interaction data
        self.repository.store_interaction(data)

    def get_interactions_by_user(self, user_id: int):
        logger = logging.getLogger(__name__)
        logger.info(f"Retrieving interactions for user ID: {user_id}")

        try:
            return self.repository.retrieve_interactions_by_user(user_id)
        except Exception as e:
            logger.error(f"Error retrieving interactions: {e}")
            raise

    def validate_data(self, data: dict) -> bool:
        required_fields = ['user_id', 'interaction_type']
        for field in required_fields:
            if field not in data or not data[field]:
                return False
        return True