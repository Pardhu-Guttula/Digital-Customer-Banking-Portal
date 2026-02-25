# Epic Title: Enforce Role-Based Access Control Using FastAPI

class Permission:
    def __init__(self, permission_id: int, permission_name: str):
        self.permission_id = permission_id
        self.permission_name = permission_name