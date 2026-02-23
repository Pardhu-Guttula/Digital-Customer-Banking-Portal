# Epic Title: Enable Users to Leave Reviews and Ratings for Products

from sqlalchemy.orm import Session
from backend.database.config import get_db
from backend.reviews_ratings.models.review import Review

def submit_review(content: str, rating: int, product_id: int, user_id: int):
    db: Session = next(get_db())
    review = Review(content=content, rating=rating, product_id=product_id, user_id=user_id)
    db.add(review)
    db.commit()
    return review