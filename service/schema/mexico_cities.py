from typing import Optional
from pydantic import BaseModel

class MexicoCities (BaseModel):
    id: Optional[int]
    name: str
    description: str
    assessment: float
    photo_url: str