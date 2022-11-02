from typing import Optional
from pydantic import BaseModel

class Activities(BaseModel):
    id: Optional[int]
    name: str
    time: str
    price: float