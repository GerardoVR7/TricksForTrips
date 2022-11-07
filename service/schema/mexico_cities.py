from typing import Optional
from pydantic import BaseModel

class MexicoCities (BaseModel):
    id: Optional[int]
    name: str