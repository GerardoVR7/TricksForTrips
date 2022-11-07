from typing import Optional
from pydantic import BaseModel

class TypeDish (BaseModel):
    id: Optional[int]
    type: str