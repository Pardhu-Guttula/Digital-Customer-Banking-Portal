# Epic Title: Develop Backend Process Workflows using FastAPI

import logging
import requests
from backend.account_opening.models.account_opening_request import AccountOpeningRequest

class CoreBankingRepository:
    def __init__(self):
        self.api_url = "http://core-banking-system/api"

    def submit_to_core_banking(self, request: AccountOpeningRequest):
        logger = logging.getLogger(__name__)
        payload = {
            "name": request.name,
            "email": request.email,
            "phone": request.phone,
            "address": request.address
        }
        
        try:
            response = requests.post(f"{self.api_url}/account_opening", json=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to submit to core banking system: {e}")
            raise