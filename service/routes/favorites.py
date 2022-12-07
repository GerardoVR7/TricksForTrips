from unittest import result
from  sqlalchemy.sql.expression import func 
from sqlalchemy import and_
from fastapi import APIRouter, Response, Depends, HTTPException
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from datetime import date
from ..schema.favorites import Favorites
from ..models.favorites import favorites
from ..auth.auth_bearer import JWTBearer

favorites_router = APIRouter()

@favorites_router.get("/favorites", tags=["Favs"])
async def get_all_favorites():
    try:
        res = conn.execute(favorites.select()).fetchall()
    except:
        raise Response(
            status_code=404,
            content="Something was wrong with the request"
        )
    if res == None or res == [] or res == {}:
        return Response(status_code=400)
    return res

@favorites_router.get("/favorites/user/{id}", tags=["Favs"])
async def get_fav_by_user(id:int):
    try:
        res = conn.execute(favorites.select().where(favorites.c.id_user == id)).fetchall()
    except:
        raise HTTPException(
            status_code=404,
            content="Something was wrong with the request"
        )
    if res == None or res == [] or res == {}:
        return Response(
            status_code=404,
            content="Item not found",
            headers={"Error" : "Data empty"}
        )
    return res

@favorites_router.post("/favorites/create", tags=["Favs"])
async def create_tours(new_fav: Favorites):

    new_fav = {
    "id": new_fav.id,
    "id_tour": new_fav.id_tour,
    "id_user": new_fav.id_user
    }

    try:
        result = conn.execute(favorites.insert().values(new_fav))
        res = conn.execute(favorites.select().where(favorites.c.id == result.lastrowid)).first()
    except:
        raise HTTPException(
            status_code=404,
            content="Something was wrong with the request"
        )
    else:
        return res

@favorites_router.delete("/favorites/delete/{id}", tags=["Favs"])
async def delete_fav(id: int):
    try:
        conn.execute(favorites.delete().where(favorites.c.id == id))
        res =  conn.execute(favorites.select().where(favorites.c.id == id)).first()
    except:
        raise HTTPException(
            status_code=404,
            content="Something was wrong with the request"
        )
    else:
        return Response(
            status_code=204,    
            content="Object deleted")