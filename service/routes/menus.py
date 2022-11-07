from fastapi import APIRouter, Response, HTTPException
from ..config.database import conn
from ..models.menus import menus
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from ..schema.menus import Menus

menus_router = APIRouter()

@menus_router.get("/menus")
def get_all_menus():
    return conn.execute(menus.select()).fetchall() 

@menus_router.get("/menus/{id}")
def get_restaurant(id : int):
    res = conn.execute(menus.select().where(menus.c.id == id)).first()
    print(res)
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")

    return conn.execute(menus.select().where(menus.c.id== id)).first()

@menus_router.post("/menus/create")
def create_menu(n_menu : Menus):
    new_menu = {
        "id_restaurant": n_menu.id_restaurant,
        "name": n_menu.name
    }
    result = conn.execute(menus.insert().values(new_menu))
    print(result.lastrowid)
    return conn.execute(menus.select().where(menus.c.id == result.lastrowid)).first()

@menus_router.delete("/menus/delete/{id}")
def delete_menu(id : int):
    res = conn.execute(menus.delete().where(menus.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)