from unittest import result
from  sqlalchemy.sql.expression import func 
from sqlalchemy import and_
from fastapi import APIRouter, Response, Depends, HTTPException
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from datetime import date
from ..schema.tours import Tours
from ..models.tours import tours as tr
from ..auth.auth_bearer import JWTBearer

tours = APIRouter()

@tours.get("/tours", tags=["Tours"])
async def get_all_tours():
    try:
        res = conn.execute(tr.select()).fetchall()
    except:
        raise Response(
            status_code=404,
            content="Something was wrong with the request"
        )
    if res == None or res == [] or res == {}:
        return Response(status_code=400)
    return res

@tours.get("/tours/random", tags=["Tours"])
async def get_all_tours():
    try:
        res = conn.execute(tr.select().order_by(func.rand())).fetchall()
        res = res[0:9]
    except:
        raise Response(
            status_code=404,
            content="Something was wrong with the request"
        )
    if res == None or res == [] or res== {}:
        return Response(
            status_code=404,
            content="Not exist data",
            headers={"Error" : "Data empty"}
        )
    return res

@tours.get("/tours/avaliable/{id_city}/{date}", tags=["Tours"])
async def get_tours_validity(id_city : int, date : date):
    try:

        res = conn.execute(tr.select().filter(and_(tr.c.id_city == id_city , tr.c.validity_start <= date , tr.c.validity_end >= date))).fetchall()
    except:
        raise HTTPException(
            status_code=404,
            detail="Something was wrong with the request"
        )
    if res == None or res == [] or res == {}:
        return Response(
            status_code=404, content="algo salio mal papito"
        )
    return res

@tours.get("/tours/agencies/{id}", tags=["Tours"])
async def get_tours_by_agency(id_agency:int):
    try:
        res = conn.execute(tr.select().where(tr.c.id_agency == id_agency)).fetchall()
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

@tours.get("/tours/{id}", tags=["Tours"])
async def search_by_city(id_city : int):
    try:
        res = conn.execute(tr.select().where(tr.c.id == id_city)).first()
    except:
        raise HTTPException(
            status_code=404,
            content="Something was wrong with the request"
        )
    if res == None or res == [] or res == {}:
        return Response(
            status_code=404,
            content="Item not found",
            headers={"Error" : "Data empty or out range"}
        )
    return res

@tours.post("/tours/create", tags=["Tours"])
async def create_tours(new_tour: Tours):

    new_tour = {
    "id": new_tour.id,
    "id_agency": new_tour.id_agency,
    "id_city":new_tour.id_city,
    "agency_name": new_tour.agency_name,
    "place_name": new_tour.place_name,
    "description": new_tour.description,
    "capacity": new_tour.capacity,
    "included_services": new_tour.included_services,
    "start_time": new_tour.start_time,
    "return_time": new_tour.return_time,
    "interest_points": new_tour.interest_points,
    "price": new_tour.price, 
    "min_number_people": new_tour.min_number_people,
    "validity_start": new_tour.validity_start,
    "validity_end": new_tour.validity_end,
    "photo_name": new_tour.photo_name,
    "photo_url": new_tour.photo_url
    }

    try:
        result = conn.execute(tr.insert().values(new_tour))
        res = conn.execute(tr.select().where(tr.c.id == result.lastrowid)).first()
    except:
        raise HTTPException(
            status_code=404,
            content="Something was wrong with the request"
        )
    else:
        return res

@tours.put("/tours/update/{id}", tags=["Tours"])
async def update_tour(id: int, edit_tour :Tours):
    try:
        conn.execute(tr.update().values(
                id_agency= edit_tour.id_agency,
                id_city= edit_tour.id_city,
                agency_name= edit_tour.agency_name,
                place_name=  edit_tour.place_name,
                description=  edit_tour.description,
                capacity= edit_tour.capacity,
                included_services= edit_tour.included_services,
                start_time= edit_tour.start_time,
                return_time= edit_tour.return_time,
                interest_points= edit_tour.interest_points,
                price= edit_tour.price,
                min_number_people= edit_tour.min_number_people,
                validity_start= edit_tour.validity_start,
                validity_end= edit_tour.validity_end,
                photo_name= edit_tour.photo_name,
                photo_url= edit_tour.photo_url
                ).where(tr.c.id == id)
            )
        res = conn.execute(tr.select().where(tr.c.id == id)).first()
        print(res)
    except:
        raise HTTPException(
            status_code=404,
            content="Something was wrong with the request"
        )
    if res == None or res == [] or res == {}:
        return Response(
            status_code=404,
            content="Item not found",
            headers={"Error" : "Data empty or out range"}
        )
    return res

@tours.delete("/tours/delete/{id}", tags=["Tours"])
async def delete_tour(id: int):
    try:
        conn.execute(tr.delete().where(tr.c.id == id))
        res =  conn.execute(tr.select().where(tr.c.id == id)).first()
    except:
        raise HTTPException(
            status_code=404,
            content="Something was wrong with the request"
        )
    else:
        return Response(
            status_code=204,    
            content="Object deleted")