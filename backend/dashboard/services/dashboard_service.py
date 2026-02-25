# Epic Title: Personalized User Dashboard for Banking Products and Services

from backend.dashboard.repositories.dashboard_repository import DashboardRepository
from backend.services.cache_service import CacheService
import logging

class DashboardService:
    def __init__(self):
        self.repository = DashboardRepository()
        self.cache_service = CacheService()

    def get_personalized_dashboard(self, user_id: int):
        cache_key = f'user_dashboard_{user_id}'
        data = self.cache_service.get(cache_key)
        
        if data is None:
            data = self.repository.fetch_user_dashboard(user_id)
            self.cache_service.set(cache_key, data)
        return data