# Epic Title: Track and Analyze Sales Data

from sqlalchemy.orm import Session
from backend.database.config import get_db
from backend.analytics_reporting.models.sales_data import SalesData
from backend.analytics_reporting.models.analytics_report import AnalyticsReport

def generate_analytics_report() -> dict:
    db: Session = next(get_db())
    sales_data = db.query(SalesData).all()
    report = aggregate_sales_data(sales_data)
    return report

def aggregate_sales_data(sales_data: list) -> dict:
    aggregated_data = {"total_revenue": 0, "total_quantity_sold": 0}
    for data in sales_data:
        aggregated_data["total_revenue"] += data.total_revenue
        aggregated_data["total_quantity_sold"] += data.quantity_sold
    return aggregated_data