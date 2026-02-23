# Epic Title: Integrate PostgreSQL Database for Data Management in the Admin Dashboard

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database.config import get_db
from backend.admin_dashboard.services.dashboard_service import get_order_stats, get_product_stats

router = APIRouter()

@router.get("/stats")
def fetch_stats(db: Session = Depends(get_db)):
    try:
        order_count = get_order_stats(db)
        product_count = get_product_stats(db)
        return {"order_count": order_count, "product_count": product_count}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))