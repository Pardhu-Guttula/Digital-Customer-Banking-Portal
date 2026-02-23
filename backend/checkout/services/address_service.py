# Epic Title: Address Entry in Checkout Process

import logging
from typing import Optional
from backend.checkout.models.address import Address

logger = logging.getLogger(__name__)

class AddressService:

    @staticmethod
    def save_address(address: Address) -> bool:
        # Logic for saving address to database
        logger.info(f"Saving address for user_id {address.user_id}")
        try:
            # Simulated save logic
            logger.info("Address data saved successfully")
            return True
        except Exception as e:
            logger.error(f"Error saving address data: {str(e)}")
            return False