# Epic Title: Store Order and Payment Information in PostgreSQL

import logging
from typing import Tuple
from backend.checkout.models.payment import Payment

logger = logging.getLogger(__name__)

class PaymentService:

    @staticmethod
    def process_payment(payment: Payment) -> Tuple[bool, str]:
        # Encrypt payment details and simulate payment processing through gateway
        logger.info(f"Processing payment for order_id {payment.order_id}")
        try:
            if payment.amount > 1000:  # Simulated fund check
                logger.error("Insufficient funds")
                return False, "Insufficient funds"
            elif len(payment.card_cvv) != 3 and len(payment.card_cvv) != 4:  # Validate CVV
                logger.error("Invalid payment information")
                return False, "Invalid payment information"
                
            # Simulated successful payment processing
            logger.info("Payment processed successfully")
            return True, "Payment processed successfully"
        except Exception as e:
            logger.error(f"Error processing payment: {str(e)}")
            return False, "Payment gateway error"