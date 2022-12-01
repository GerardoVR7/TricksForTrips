from unittest import result
from fastapi import APIRouter, HTTPException, Response, Depends
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from datetime import date
from ..schema.bookings import Booking
from ..models.bookings import booking
from ..auth.auth_bearer import JWTBearer

booking_router = APIRouter()

@booking_router.get("/bookings", tags=["Bookings"])
async def get_all_bookings():
    try:
        res = conn.execute(booking.select()).fetchall()
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

@booking_router.get("/bookings/user/{id}", tags=["Bookings"])
async def get_bookings_by_user(id:int):
    try:
        res = conn.execute(booking.select().where(booking.c.id_tourist == id)).fetchall()
    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the request"
        )
    if res == None or res == []:
        return Response(
            status_code=404,
            detail="Item not found",
            headers={"Error" : "Data empty"}
        )
    return res

@booking_router.get("/bookings/agency/{id}", tags=["Bookings"])
async def get_bookings_by_agency(id:int):
    try:
        res = conn.execute(booking.select().where(booking.c.id_agency == id)).fetchall()
    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the request"
        )
    if res == None or res == []:
        return Response(
            status_code=404,
            detail="Item not found",
            headers={"Error" : "Data empty"}
        )
    return res

@booking_router.post("/bookings/create", tags=["Bookings"])
async def create_booking(new_booking: Booking):

    new_booking = {
        "id": new_booking.id,
        "id_tourist": new_booking.id_tourist,
        "id_tour": new_booking.id_tour,
        "id_agency": new_booking.id_agency,
        "tourist_name": new_booking.tourist_name,
        "date": new_booking.date,
        "adults": new_booking.adults,
        "childrens": new_booking.childrens,
        "babys": new_booking.babys,
        "pets": new_booking.pets,
        "total": new_booking.total
    }

    try:
        result = conn.execute(booking.insert().values(new_booking))
        res = conn.execute(booking.select().where(booking.c.id == result.lastrowid)).first()
    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the request",
            headers={"Error": "checa el formato kramky, sino esta mal algo en back con los paramaetros"}
        )
    else:
        return res

@booking_router.put("/bookings/update/{id}", tags=["Bookings"])
async def update_booking(id:int, edit_booking: Booking):
    try:
        conn.execute(booking.update().value(
            id_tourist= edit_booking.id_tourist,
            id_tour= edit_booking.id_tour,
            id_agency= edit_booking.id_agency,
            tourist_name= edit_booking.tourist_name,
            date= edit_booking.date,
            adults= edit_booking.adults,
            childrens= edit_booking.childrens,
            babys= edit_booking.babys,
            pets= edit_booking.pets,
            total= edit_booking.total
            ).where(booking.c.id == id)
        )
        res = conn.execute(
                booking.select().where(booking.c.id == id)
            ).first()
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

@booking_router.delete("/bookings/delete/{id}", tags=["Bookings"])
async def delete_booking(id:int):
    try:
        conn.execute(booking.delete().where(booking.c.id == id))
        res =  conn.execute(booking.select().where(booking.c.id == id)).first()
    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the request"
        )
    else:
        return Response(
            status_code=204,    
            detail="Object deleted")