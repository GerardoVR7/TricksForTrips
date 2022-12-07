from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Paypal(BaseModel):
    id: Optional[int]
    id_user: int
    id_paypal: int
    date: datetime
    total: float