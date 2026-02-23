# Epic Title: Add Product to Shopping Cart

import logging
from backend.shopping_cart.models.cart import Cart, CartItem
from backend.product_listings.models.product import Product

logger = logging.getLogger(__name__)

class CartService:

    @staticmethod
    def add_item_to_cart(cart_item: CartItem) -> bool:
        # Placeholder logic for adding item to cart
        logger.info(f"Adding product {cart_item.product_id} to cart with quantity {cart_item.quantity}")
        # Simulated stock check
        if cart_item.product_id == 101 and cart_item.quantity <= 5:
            logger.info(f"Product {cart_item.product_id} added to cart successfully")
            # Update cart database/entities as necessary
            return True
        logger.error(f"Product {cart_item.product_id} is out of stock or insufficient quantity available")
        return False