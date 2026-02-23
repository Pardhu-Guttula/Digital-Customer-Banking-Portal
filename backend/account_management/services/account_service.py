# Epic Title: Develop streamlined workflows for submitting account opening requests

from backend.account_management.repositories.account_repository import AccountRepository

class AccountService:
    def __init__(self, db):
        self.account_repository = AccountRepository(db)

    def process_opening_request(self, data: dict) -> dict:
        required_fields = ['name', 'email', 'phone']
        
        for field in required_fields:
            if field not in data or not data[field]:
                return {"success": False, "message": f"Missing mandatory field: {field}"}
        
        try:
            self.account_repository.save_account_opening_request(data)
            return {"success": True, "message": "Request processed"}
        except Exception as e:
            return {"success": False, "message": "Backend processing error"}