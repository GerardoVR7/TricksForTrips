from typing import Optional
from pydantic import BaseModel

class Dishes(BaseModel):
    id: Optional[int]
    id_menu: int
    id_type: int
    name: str
    description: str
    principal_ingredient: str
    price: float