# Epic Title: Dynamic and Interactive Dashboard UI using React

from backend.dashboard.repositories.dashboard_repository import DashboardRepository

class DashboardService:
    def __init__(self, db):
        self.dashboard_repository = DashboardRepository(db)

    def fetch_dashboard_data(self, user_id: str):
        user_profile = self.dashboard_repository.get_user_profile(user_id)
        
        if not user_profile:
            return None
        
        banking_products = self.dashboard_repository.get_banking_products(user_profile)
        services = self.dashboard_repository.get_services(user_profile)

        return {
            "user_profile": user_profile,
            "banking_products": banking_products,
            "services": services
        }