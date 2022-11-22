from unittest import result
from fastapi import APIRouter, Response, HTTPException
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from ..schema.activities import Activities
from ..models.activities import activities as ac

activities = APIRouter()

@activities.get("/activities")
def get_all_activities():
    return conn.execute(ac.select()).fetchall()


@activities.post("/activities/create")
async def create_activity(new_activity: Activities):
    new_activity = {
        "id": new_activity.id,
        "name": new_activity.name,
        "time": new_activity.time,
        "price": new_activity.price
    }
    result = conn.execute(ac.insert().values(new_activity))
    print(result.lastrowid)
    return conn.execute(ac.select().where(ac.c.id == result.lastrowid)).first()

