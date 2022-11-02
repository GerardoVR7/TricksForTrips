from typing import Optional
from pydantic import BaseModel

class Restaurants (BaseModel):
    id: Optional[int]
    name: str
    description:str
    address: str
    RFC: str
    email: str
    password: str
    url: str
    cellphone: str
    postal_code: int