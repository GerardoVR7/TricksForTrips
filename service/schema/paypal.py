from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Paypal(BaseModel):
    id: Optional[int]
    id_user: int
    id_paypal: str
    date: datetime
    total: float