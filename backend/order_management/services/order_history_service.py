# Epic Title: Allow Users to View Order History

import logging
from typing import List, Dict
from backend.order_management.models.order import Order, OrderItem, OrderStatus

logger = logging.getLogger(__name__)

class OrderHistoryService:

    @staticmethod
    def get_order_history(user_id: int, sort_by_date: bool) -> List[Dict]:
        # Simulated retrieval logic for order history
        logger.info(f"Retrieving order history for user_id {user_id}")
        try:
            history = [
                Order(id=1, user_id=user_id, address_id=1, items=[OrderItem(product_id=101, quantity=2, price=29.99)], total_amount=59.98, status=OrderStatus(id=1, status="Delivered"), date="2023-09-01").dict(),
                Order(id=2, user_id=user_id, address_id=1, items=[OrderItem(product_id=102, quantity=1, price=49.99)], total_amount=49.99, status=OrderStatus(id=2, status="Pending"), date="2023-10-01").dict(),
            ]

            if sort_by_date:
                history.sort(key=lambda x: x['date'], reverse=True)

            return history
        except Exception as e:
            logger.error(f"Error retrieving order history: {str(e)}")
            raise