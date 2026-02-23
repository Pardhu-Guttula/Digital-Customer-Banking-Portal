# Epic Title: Product Listing Page

import logging
from typing import List, Dict
from backend.product_listings.models.product import Product

logger = logging.getLogger(__name__)

class ProductService:

    @staticmethod
    def get_all_products(page: int, per_page: int) -> List[Dict]:
        # Placeholder for actual product retrieval logic
        logger.info(f"Fetching products for page {page} with {per_page} items per page")
        # Simulated product list
        products = [{"id": 1, "name": "Product A", "description": "Description A", "price": 10.00, "stock_quantity": 100},
                    {"id": 2, "name": "Product B", "description": "Description B", "price": 20.00, "stock_quantity": 200}]
        return products[(page-1)*per_page: page*per_page]