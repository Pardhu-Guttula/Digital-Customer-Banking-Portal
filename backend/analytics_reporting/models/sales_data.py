# Epic Title: Data Storage and Retrieval Using PostgreSQL

from sqlalchemy import Column, Integer, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.config import Base

class SalesData(Base):
    __tablename__ = 'sales_data'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    total_revenue = Column(Float, nullable=False)
    sale_timestamp = Column(TIMESTAMP, nullable=False)

    product = relationship("Product")