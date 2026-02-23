# Epic Title: Develop Product Listing Page

import logging
from backend.product_listings.models.product import Product

logger = logging.getLogger(__name__)

class ProductService:

    @staticmethod
    def add_product(product: Product) -> None:
        # Placeholder for actual product addition logic
        # This is where we would handle database interaction to save the product details
        logger.info(f"Adding product: {product.name}")