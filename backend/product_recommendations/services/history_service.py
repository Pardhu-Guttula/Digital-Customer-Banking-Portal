# Epic Title: Store User Activity Data in PostgreSQL

from sqlalchemy.orm import Session
from backend.database.models import BrowsingHistory, PurchaseHistory

def log_browsing_history(db: Session, user_id: int, product_id: int):
    browsing_history = BrowsingHistory(user_id=user_id, product_id=product_id, viewed_at=datetime.utcnow())
    db.add(browsing_history)
    db.commit()
    return browsing_history

def log_purchase_history(db: Session, user_id: int, product_id: int):
    purchase_history = PurchaseHistory(user_id=user_id, product_id=product_id, purchased_at=datetime.utcnow())
    db.add(purchase_history)
    db.commit()
    return purchase_history