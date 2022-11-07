from fastapi import APIRouter, Response, HTTPException
from config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.tourist import Tourist
from models.tourist import tourist

tourist_router = APIRouter()

@tourist_router.get("/turists")
async def get_all_tourist():
    return conn.execute(tourist.select()).fetchall()

@tourist_router.post("/tourists/new")
async def create_tourist(new_tourist: Tourist):
    new_tourist = {
        "id": new_tourist.id,
        "name": new_tourist.name,
        "lastname": new_tourist.lastname,
        "email": new_tourist.email,
        "password": new_tourist.password,
        "phone": new_tourist.phone,
        "address": new_tourist.address,
        "postal_code": new_tourist.postal_code,
        "country": new_tourist.country
    }

    result = conn.execute(tourist.insert().values(new_tourist))
    print(result.lastrowid)
    return conn.execute(tourist.select().where(tourist.c.id == result.lastrowid)).first()

