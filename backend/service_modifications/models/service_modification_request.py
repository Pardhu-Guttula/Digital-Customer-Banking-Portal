# Epic Title: Implement FastAPI Backend for Handling Service Modification Requests

from pydantic import BaseModel

class ServiceModificationRequest(BaseModel):
    user_id: int
    service_type: str
    modification_details: str