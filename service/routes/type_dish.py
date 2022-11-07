from fastapi import APIRouter, Response, HTTPException

from config.database import conn
from models.type_dish import type_dish 
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.type_dish import TypeDish

type_dish_router = APIRouter()

@type_dish_router.get("/type_dish")
def get_all_type_of_dish():
    return conn.execute(type_dish.select()).fetchall() 

@type_dish_router.get("/type_dish/{id}")
def get_type_dish(id : int):
    res = conn.execute(type_dish.select().where(type_dish.c.id == id)).first()
    print(res)
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")
    return conn.execute(type_dish.select().where(type_dish.c.id== id)).first()

@type_dish_router.post("/type_dish/create")
def create_type_of_dish(n_type_dish : TypeDish):
    new_type_dish = {
        "type": n_type_dish.type
    }
    result = conn.execute(type_dish.insert().values(new_type_dish))
    print(result.lastrowid)
    return conn.execute(type_dish.select().where(type_dish.c.id == result.lastrowid)).first()

@type_dish_router.delete("/type_dish/delete/{id}")
def delete_type_dish(id : int):
    res = conn.execute(type_dish.delete().where(type_dish.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)