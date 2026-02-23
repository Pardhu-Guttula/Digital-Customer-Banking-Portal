# Epic Title: Implement Product Recommendations Based on User Preferences

from sqlalchemy.orm import Session
from backend.database.config import get_db
from backend.product_recommendations.models.recommendation import Recommendation
from backend.product_listings.models.product import Product

def generate_recommendations(user_id: int) -> list:
    db: Session = next(get_db())
    user_history = db.query(Product).join(Recommendation).filter(Recommendation.user_id == user_id).all()
    recommendations = calculate_recommendations(user_history)
    store_recommendations(db, user_id, recommendations)
    return recommendations

def calculate_recommendations(user_history: list) -> list:
    # Placeholder for actual recommendation logic based on user history
    return user_history

def store_recommendations(db: Session, user_id: int, recommendations: list):
    for product in recommendations:
        db_recommendation = Recommendation(user_id=user_id, product_id=product.id)
        db.add(db_recommendation)
    db.commit()