# Epic Title: Capture and maintain a history of user interactions

from backend.history.repositories.user_interaction_repository import UserInteractionRepository

class UserInteractionService:
    def __init__(self, db):
        self.user_interaction_repository = UserInteractionRepository(db)

    def record_interaction(self, data: dict):
        user_id = data.get('user_id')
        action = data.get('action')
        timestamp = data.get('timestamp')

        if not user_id or not action or not timestamp:
            raise ValueError('Missing required fields: user_id, action, timestamp')
        
        self.user_interaction_repository.save_interaction({
            'user_id': user_id,
            'action': action,
            'timestamp': timestamp
        })