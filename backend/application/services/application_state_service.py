# Epic Title: Save incomplete application state

from backend.application.repositories.application_state_repository import ApplicationStateRepository

class ApplicationStateService:
    def __init__(self, db):
        self.application_state_repository = ApplicationStateRepository(db)

    def save_state(self, data: dict):
        user_id = data.get('user_id')
        state = data.get('state')

        if not user_id or not state:
            raise ValueError('Missing required fields: user_id, state')
        
        self.application_state_repository.save_state({
            'user_id': user_id,
            'state': state
        })

    def load_state(self, user_id: str):
        if not user_id:
            raise ValueError('Missing required field: user_id')
        
        return self.application_state_repository.load_state(user_id)