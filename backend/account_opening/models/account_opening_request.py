# Epic Title: Enable Users to Submit Account Opening Requests through Streamlined Workflows

from pydantic import BaseModel

class AccountOpeningRequest(BaseModel):
    name: str
    email: str
    phone: str
    address: str