from typing import Optional
from datetime import date
from pydantic import BaseModel
from typing import Dict


class Customer (BaseModel):
    external_id:str
    name:str
    last_name:str
    email:str
    requires_account: bool
    phone_number:str
    address:Dict[str:str] = None
    