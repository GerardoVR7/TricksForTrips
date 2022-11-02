from datetime import time
from typing import Optional
from pydantic import BaseModel

class Tours (BaseModel):
    id: Optional[int]
    id_agency: int
    id_activity: int
    place_name: str
    description: str
    capacity: int
    included_services: str
    start_time: time
    return_time: time
    interest_points: str
    price: float
    min_number_people: int
    location: str