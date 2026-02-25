# Epic Title: Integrate PostgreSQL for Storing Service Modification Request Details

from pydantic import BaseModel, Field
from typing import Optional

class ServiceModificationRequest(BaseModel):
    user_id: int
    service_type: str
    modification_details: str
    status: Optional[str] = Field(default="Pending")