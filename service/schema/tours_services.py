from typing import Optional
from pydantic import BaseModel

class ToursServices (BaseModel):
    id: Optional[int]
    name: str