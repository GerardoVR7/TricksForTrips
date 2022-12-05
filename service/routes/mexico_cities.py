from unittest import result
from fastapi import APIRouter, Response, HTTPException, Depends
from  sqlalchemy.sql.expression import func, select
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from ..schema.mexico_cities import MexicoCities
from ..models.mexico_cities import mexico_cities
from ..auth.auth_bearer import JWTBearer

mexico_cities_router = APIRouter()

@mexico_cities_router.get("/mexico/cities", tags=["Cities"])
async def get_all_mexico_cities():
    try:
        res = conn.execute(mexico_cities.select()).fetchall()
    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the request"
        )
    if res == None or res == []:
        return Response(
            status_code=404,
            detail="Not exist data",
            headers={"Error" : "Data empty"}
        )
    return res

@mexico_cities_router.post("/mexico/cities/new", tags=["Cities"])
async def add_new_city(new_city : MexicoCities):
    new_city = {
        "id": new_city.id,
        "name": new_city.name,
        "description": new_city.description,
        "assessment": new_city.assessment,
        "photo_url": new_city.photo_url
    }
    try:
        result = conn.execute(mexico_cities.insert().values(new_city))
        res = conn.execute(mexico_cities.select().where(mexico_cities.c.id == result.lastrowid)).first()
    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the post"
        )
    else:
        return res

@mexico_cities_router.put("/mexico/cities/update/{id}", tags=["Cities"])
async def update_city(id: int, edit_mexico_city: MexicoCities):
    try:
        conn.execute(mexico_cities.update().values(
        name= edit_mexico_city.name,
        description= edit_mexico_city.description,
        assessment= edit_mexico_city.assessment,
        photo_url= edit_mexico_city.photo_url
            ).where(mexico_cities.c.id == id)
        )
        res = conn.execute(mexico_cities.select().where(mexico_cities.c.id == id)).first()
    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the request"
        )
    if res == None or res == [] or res == {}:
        return Response(
            status_code=404,
            detail="Item not found",
            headers={"Error" : "Data empty or out range"}
        )
    return res

@mexico_cities_router.delete("/mexico/cities/delete/{id}", tags=["Cities"])
async def delete_city(id:int):
    try:
        conn.execute(mexico_cities.delete().where(mexico_cities.c.id == id))
    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the request"
        )
    else:
        return Response(
            status_code=204,
            detail="Object deleted")