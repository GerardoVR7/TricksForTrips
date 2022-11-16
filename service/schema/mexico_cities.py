from typing import Optional
from pydantic import BaseModel
from typing import Dict


class MexicoCities (BaseModel):
    id: Optional[int]
    name: str
    description: str
    assessment: Dict[str, float] = None
    photo_url: str