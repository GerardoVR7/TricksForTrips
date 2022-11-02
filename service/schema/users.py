from typing import Optional
from pydantic import BaseModel

class Users(BaseModel):
    id: Optional[int]
    email: str
    password: str