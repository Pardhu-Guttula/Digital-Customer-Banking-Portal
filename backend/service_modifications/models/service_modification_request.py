# Epic Title: Develop React UI for Submitting Service Modification Requests

from pydantic import BaseModel

class ServiceModificationRequest(BaseModel):
    user_id: int
    service_type: str
    modification_details: str