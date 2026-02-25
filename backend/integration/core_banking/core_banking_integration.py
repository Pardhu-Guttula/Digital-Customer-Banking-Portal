# Epic Title: Backend Process Workflows for Account Opening

import requests
import logging
from pydantic import BaseModel

class CoreBankingIntegration:
    def __init__(self):
        self.endpoint = "https://corebanking.example.com/api/account_opening"

    def submit_request(self, request: BaseModel) -> dict:
        logger = logging.getLogger(__name__)
        logger.info("Submitting request to core banking system")

        payload = request.dict()
        response = requests.post(self.endpoint, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()