from unittest import result
from fastapi import APIRouter, Response, HTTPException
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from ..schema.mexico_cities import MexicoCities
from ..models.mexico_cities import mexico_cities

mexico_cities_router = APIRouter()

@mexico_cities_router.get("/mexico/cities")
async def get_all_mexico_cities():
    return conn.execute(mexico_cities.select()).fetchall()

@mexico_cities_router.post("/mexico/cities/new")
async def add_new_city(new_city : MexicoCities):
    new_city = {
        "id": new_city.id,
        "name": new_city.name,
        "description": new_city.description,
        "assessment": new_city.assessment,
        "photo_url": new_city.photo_url
    }
    result = conn.execute(mexico_cities.insert().values(new_city))
    print(result.lastrowid)
    return conn.execute(mexico_cities.select().where(mexico_cities.c.id == result.lastrowid)).first()