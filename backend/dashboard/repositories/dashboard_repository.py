# Epic Title: Personalized Dashboard Layout

from sqlalchemy.orm import Session

class DashboardRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_user_profile(self, user_id: str):
        # Fetch user profile data from database
        return self.db_session.execute(
            "SELECT * FROM user_profiles WHERE user_id = :user_id",
            {"user_id": user_id}
        ).fetchone()

    def get_banking_products(self, user_profile):
        # Fetch banking products based on user's profile
        eligibility_criteria = user_profile['eligibility_criteria']
        return self.db_session.execute(
            "SELECT * FROM banking_products WHERE eligibility_criteria = :eligibility_criteria",
            {"eligibility_criteria": eligibility_criteria}
        ).fetchall()

    def get_services(self, user_profile):
        # Fetch services based on user's profile
        user_preferences = user_profile['preferences']
        return self.db_session.execute(
            "SELECT * FROM services WHERE preference IN :preferences",
            {"preferences": user_preferences}
        ).fetchall()