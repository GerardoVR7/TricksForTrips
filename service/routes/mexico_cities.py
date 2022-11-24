from unittest import result
from fastapi import APIRouter, Response, HTTPException
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from ..schema.mexico_cities import MexicoCities
from ..models.mexico_cities import mexico_cities

mexico_cities_router = APIRouter()

@mexico_cities_router.get("/mexico/cities", tags=["Cities"])
async def get_all_mexico_cities():
    return conn.execute(mexico_cities.select()).fetchall()

@mexico_cities_router.post("/mexico/cities/new", tags=["Cities"])
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

@mexico_cities_router.put("/mexico/cities/update/{id}", tags=["Cities"])
async def update_city(id: int, edit_mexico_city: MexicoCities):
    conn.execute(mexico_cities.update().values(
    name= edit_mexico_city.name,
    description= edit_mexico_city.description,
    assessment= edit_mexico_city.assessment,
    photo_url= edit_mexico_city.photo_url
        ).where(mexico_cities.c.id == id)
    )
    return conn.execute(mexico_cities.select().where(mexico_cities.c.id == id))

@mexico_cities_router.delete("/mexico/cities/delete/{id}", tags=["Cities"])
async def delete_city(id:int):
    res = conn.execute(mexico_cities.delete().where(mexico_cities.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")
    else: return Response(status_code=HTTP_204_NO_CONTENT)