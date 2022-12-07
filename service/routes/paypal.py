from fastapi import APIRouter, Request
import os
from fastapi.responses import JSONResponse
import requests
from ..schema.paypal import Paypal
from ..models.paypal import paypal
from ..config.database import conn
from fastapi import APIRouter, HTTPException, Response, Depends

payment_routes = APIRouter()

@payment_routes.get("/payments", tags=["Paypal"])
async def get_all_payments():
    try:
        res = conn.execute(paypal.select()).fetchall()
    except:
        raise Response(
            status_code=404,
            content="Something was wrong with the request"
        )
    if res == None or res == []:
        return Response(
            status_code=404, 
            content="Not exist data",
            headers={"Error" : "Data empty"}
        )
    return res

@payment_routes.post("/payments/create", tags=["Paypal"])
async def create_payment(new_payment:Paypal):
    
    new_payment = {
        "id": new_payment.id,
        "id_user": new_payment.id_user,
        "id_paypal": new_payment.id_paypal,
        "date": new_payment.date,
        "total": new_payment.total
    }

    try:
        result = conn.execute(paypal.insert().values(new_payment))
        res = conn.execute(paypal.select().where(paypal.c.id == result.lastrowid)).first()
    except:
        raise Response(
            status_code=404,
            content="Something was wrong with the request",
            headers={"Error": "checa el formato kramky, sino esta mal algo en back con los paramaetros"}
        )
    else:
        return res

@payment_routes.delete("/payments/delete/{id}", tags=["Paypal"])
async def delete_payment(id:int):
    try:
        conn.execute(paypal.delete().where(paypal.c.id == id))
        res =  conn.execute(paypal.select().where(paypal.c.id == id)).first()
    except:
        raise Response(
            status_code=404,
            content="Something was wrong with the request"
        )
    else:
        return Response(
            status_code=204,    
            content="Object deleted")