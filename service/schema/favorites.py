from datetime import time
from typing import Optional
from typing import Dict
from datetime import date
from pydantic import BaseModel

class Favorites(BaseModel):
    id: Optional[int]
    id_tour: int
    id_user: int