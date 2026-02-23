# Epic Title: Integrate PostgreSQL Database for Data Management in the Admin Dashboard

from sqlalchemy.orm import Session
from backend.database.models import Order, Product

def get_order_stats(db: Session):
    return db.query(Order).count()

def get_product_stats(db: Session):
    return db.query(Product).count()