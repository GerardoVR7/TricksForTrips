from typing import Optional
from pydantic import BaseModel

class Agencies (BaseModel):
    id: Optional[int]
    name: str
    address: str
    RFC: str
    email: str
    password: str
    url: str
    agency_code: str
    phone: str
    postal_code: int