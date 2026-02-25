# Epic Title: Secure Role-Based Data Segregation in PostgreSQL

from backend.rbac.repositories.data_repository import DataRepository
import logging

class DataService:
    def __init__(self):
        self.repository = DataRepository()

    def get_data_for_role(self, role: str) -> list:
        logger = logging.getLogger(__name__)
        logger.info(f"Retrieving data for role: {role}")
        return self.repository.get_data_for_role(role)

    def insert_data(self, data: str, role: str):
        logger = logging.getLogger(__name__)
        logger.info(f"Inserting data for role: {role}")
        self.repository.insert_data(data, role)