from unittest import result
from typing import Dict
from fastapi import APIRouter, HTTPException, Response, Depends
from ..config.database import conn
from ..schema.customer import Customer
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from datetime import date
import os
import openpay
import requests

openpay.api_key = os.environ["OPENPAY_KEY"]
openpay.verify_ssl_certs = False
openpay.merchant_id = os.environ["OPENPAY_MERCHANT"]

openpay_router =  APIRouter()
url = 'https://sandbox-api.openpay.mx/v1/m3zwajjoabqmrgg9dk3p/'
@openpay_router.post(url, tags=["Payments"])
async def create_booking(token : Customer):

    try:
        print(token)
        customer = openpay.Customer.create(token)
        print(customer)
    
    except:
        raise HTTPException(
            status_code=404,
            detail="Something was wrong with the request"
        )
    else:
        raise Response(status_code=200, content={"message":"va bien papito", "openpay":customer})