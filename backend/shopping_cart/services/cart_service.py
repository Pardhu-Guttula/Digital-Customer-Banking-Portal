# Epic Title: Remove Product from Shopping Cart

import logging
from backend.shopping_cart.models.cart import CartItem

logger = logging.getLogger(__name__)

class CartService:

    @staticmethod
    def remove_item_from_cart(cart_item: CartItem) -> bool:
        # Placeholder logic for removing item from cart
        logger.info(f"Removing product {cart_item.product_id} from cart")
        # Simulated cart removal logic
        if cart_item.product_id == 101:
            logger.info(f"Product {cart_item.product_id} removed from cart successfully")
            # Update cart database/entities as necessary
            return True
        logger.error(f"Product {cart_item.product_id} not found in cart")
        return False