from unittest import result
from fastapi import APIRouter, Response, HTTPException
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from ..schema.tours_services import ToursServices
from ..models.tours_serivices import tours_services

tours_services_router = APIRouter()

@tours_services_router.get("/tours/services", tags=["Tours Services"])
async def get_all_tours_services():
    return conn.execute(tours_services.select()).fetchall()

@tours_services_router.post("/tours/services/new")
async def create_tour_serivce(new_tour_service : ToursServices):
    new_tour_service = {
        "id": new_tour_service.id,
        "name": new_tour_service.name
    }
    result = conn.execute(tours_services.insert().values(new_tour_service))
    print(result.lastrowid)
    return conn.execute(tours_services.select().where(tours_services.c.id == result.lastrowid)).first()

@tours_services_router.put("/tours/services/update/{id}", tags=["Tours Services"])
async def update_tour(id:int, edit_tour_service: ToursServices):
    conn.execute(tours_services.update().values(
        name= edit_tour_service.name
        ).where(tours_services.c.id == id)
    )
    return conn.execute(tours_services.select().where(tours_services.c.id == id))

@tours_services_router.delete("/tours/serivces/delete/{id}", tags=["Tours Services"])
async def delete_tour_service(id:int):
    res = conn.execute(tours_services.delete().where(tours_services.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")
    else: return Response(status_code=HTTP_204_NO_CONTENT)