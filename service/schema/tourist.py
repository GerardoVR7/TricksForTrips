from typing import Optional
from pydantic import BaseModel

class Tourist (BaseModel):
    id: Optional[int]
    name: str
    lastname: str
    email: str
    password: str
    phone: str
    address: str
    postal_code: int
    country: str