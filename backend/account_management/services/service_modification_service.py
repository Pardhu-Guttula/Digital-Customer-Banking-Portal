# Epic Title: Develop streamlined workflows for submitting service modification requests

from backend.account_management.repositories.service_modification_repository import ServiceModificationRepository

class ServiceModificationService:
    def __init__(self, db):
        self.service_modification_repository = ServiceModificationRepository(db)

    def process_modification_request(self, data: dict) -> dict:
        required_fields = ['service_name', 'modification_details']
        
        for field in required_fields:
            if field not in data or not data[field]:
                return {"success": False, "message": f"Missing mandatory field: {field}"}
        
        try:
            self.service_modification_repository.save_service_modification_request(data)
            return {"success": True, "message": "Request processed"}
        except Exception as e:
            return {"success": False, "message": "Backend processing error"}