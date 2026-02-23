# Epic Title: Order Confirmation Display After Successful Purchase

import logging
from typing import Dict
from backend.order_management.models.order import OrderItem, Order

logger = logging.getLogger(__name__)

class ConfirmationService:

    @staticmethod
    def get_order_confirmation(order_id: int) -> Dict:
        # Simulated retrieval logic for order confirmation
        logger.info(f"Retrieving order confirmation for order_id {order_id}")
        try:
            order_items = [
                OrderItem(product_id=101, quantity=2, price=29.99),
                OrderItem(product_id=102, quantity=1, price=49.99)
            ]
            order = Order(id=order_id, user_id=1, address_id=1, items=order_items, total_amount=109.97)
            confirmation = {
                "order_number": order.id,
                "items": [{"product_id": item.product_id, "quantity": item.quantity, "price": item.price} for item in order.items],
                "total_amount": order.total_amount,
                "delivery_information": "Your order will be delivered to the provided address within 3-5 business days."
            }
            return confirmation
        except Exception as e:
            logger.error(f"Error retrieving order confirmation: {str(e)}")
            raise