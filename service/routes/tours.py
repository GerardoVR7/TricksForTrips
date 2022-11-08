from unittest import result
from fastapi import APIRouter, Response, HTTPException
from config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.tours import Tours
from models.tours import tours as tr

from datetime import date

tours = APIRouter()

@tours.get("/tours")
async def get_all_tours():
    return conn.execute(tr.select()).fetchall()

@tours.get("/tours/avaliable/{place}/{date}")
async def get_tours_validity(place : str, date : date):
    #print("fecha de hoy " + str(date))
    res = conn.execute(tr.select().where(
        tr.c.validity_start >= date,  tr.c.validity_start <= date, tr.c.place_name == place)).fetchall()
    #print("respuesta del back: " + str(res))
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")
    else: return res


@tours.get("/tours/{id}")
async def search_by_city(id_city : int):
    res = conn.execute(tr.select().where(tr.c.id == id_city)).first()
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")
    return res

@tours.post("/tours/create")
async def create_tours(new_tour: Tours):
    new_tour = {
    "id": new_tour.id,
    "id_agency": new_tour.id_agency,
    "id_activity": new_tour.id_activity,
    "place_name": new_tour.place_name,
    "description": new_tour.description,
    "capacity": new_tour.capacity,
    "inclued_services": new_tour.included_services,
    "start_time": new_tour.start_time,
    "return_time": new_tour.return_time,
    "interest_points": new_tour.interest_points,
    "price": new_tour.price, 
    "min_number_people": new_tour.min_number_people,
    "location": new_tour.id_city,
    "validity_start": new_tour.validity_start,
    "validity_end": new_tour.validity_end
    }
    result = conn.execute(tr.insert().values(new_tour))
    print(result.lastrowid)
    return conn.execute(tr.select().where(tr.c.id == result.lastrowid)).first()
