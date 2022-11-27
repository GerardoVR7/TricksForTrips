from typing import Optional
from datetime import date
from pydantic import BaseModel

class Booking (BaseModel):
    id: Optional[int]
    id_tourist: int
    id_tour: int
    id_agency: int
    tourist_name: str
    date: date
    adults: int
    childrens: int
    babys: int
    pets: int
    total: float
