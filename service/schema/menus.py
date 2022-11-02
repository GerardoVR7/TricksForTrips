from typing import Optional
from pydantic import BaseModel

class Menus(BaseModel):
    id: Optional[int]
    id_restaurant: int
    name: str