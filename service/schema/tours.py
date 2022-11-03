from datetime import time
from typing import Optional
from typing import Dict
from datetime import date
from pydantic import BaseModel

class Tours (BaseModel):
    id: Optional[int]
    id_agency: int
    id_activity: int
    place_name: str
    description: str
    capacity: int
    included_services: Dict[str, str] = None
    start_time: time
    return_time: time
    interest_points: str
    price: float
    min_number_people: int
    location: str
    validity_start: date
    validity_end: date