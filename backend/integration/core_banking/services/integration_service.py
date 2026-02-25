# Epic Title: Integrate Self-Service Portal with Core Banking System

from backend.integration.core_banking.repositories.integration_repository import IntegrationRepository
import logging

class IntegrationService:
    def __init__(self):
        self.repository = IntegrationRepository()

    def sync_data(self):
        logger = logging.getLogger(__name__)
        try:
            local_data = self.repository.get_local_data()
            external_data = self.repository.get_external_data()

            # Compare and sync data
            for data in local_data:
                if data not in external_data:
                    self.repository.update_external_system(data)
            
            for data in external_data:
                if data not in local_data:
                    self.repository.update_local_system(data)

            logger.info("Data synchronization completed successfully")
        except Exception as e:
            logger.error(f"Error while syncing data: {e}")
            raise