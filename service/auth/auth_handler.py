import time
from typing import Dict
import os
import jwt

JWT_SECRET = os.environ["SECRET"]
JWT_ALGORITHM = os.environ["ALGORITHM"]

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token[os.environ["DECODE"]] >= time.time() else None
    except:
        return {}