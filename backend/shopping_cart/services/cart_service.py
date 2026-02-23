# Epic Title: Persist Shopping Cart Data in PostgreSQL

import logging
from typing import Optional
from backend.shopping_cart.models.cart import Cart, CartItem

logger = logging.getLogger(__name__)

class CartService:

    @staticmethod
    def update_cart(cart: Cart) -> bool:
        # Logic for updating cart in PostgreSQL
        logger.info(f"Persisting cart for user_id {cart.user_id}")
        try:
            # Simulated persistence logic
            logger.info("Cart data persisted")
            return True
        except Exception as e:
            logger.error(f"Error persisting cart data: {str(e)}")
            return False

    @staticmethod
    def get_cart_by_user_id(user_id: int) -> Optional[Cart]:
        # Logic for retrieving cart data from PostgreSQL
        logger.info(f"Retrieving cart for user_id {user_id}")
        try:
            # Simulated retrieval logic
            items = [CartItem(id=1, product_id=101, quantity=2)]
            cart = Cart(id=1, user_id=user_id, items=items)
            return cart
        except Exception as e:
            logger.error(f"Error retrieving cart data: {str(e)}")
            return None