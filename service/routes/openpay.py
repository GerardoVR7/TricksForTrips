from unittest import result
from typing import Dict
from fastapi import APIRouter, HTTPException, Response, Depends
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from datetime import date
import os
import openpay
import requests

openpay.api_key = os.environ["OPENPAY_KEY"]
openpay.verify_ssl_certs = False
openpay.merchant_id = os.environ["OPENPAY_MERCHANT"]
openpay.production = False  # By default this works in sandbox mode

openpay_router =  APIRouter()
@openpay_router.post('https://sandbox-api.openpay.mx/v1/m3zwajjoabqmrgg9dk3p/', tags=["Payments"])
async def create_booking(token):

    try:
        print(token)
        customer = openpay.Customer.create(
            name="Juan",
            email="somebody@example.com",
            address={
                "city": "Queretaro",
                "state": "Queretaro",
                "line1": "Calle de las penas no 10",
                "postal_code": "76000",
                "line2": "col. san pablo",
                "line3": "entre la calle de la alegria y la calle del llanto",
                "country_code": "MX"
            },
            last_name="Perez",
            phone_number="44209087654")
        print(customer)
    
    except:
        raise HTTPException(
            status_code=404,
            detail="Something was wrong with the request"
        )
    else:
        raise Response(status_code=200, content={"message":"va bien papito", "openpay":customer})