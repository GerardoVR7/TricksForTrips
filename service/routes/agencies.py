
from fastapi import APIRouter, Response, HTTPException
from config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.agencies import Agencies
from models.agencies import agencies as ag

agencies = APIRouter()

@agencies.get("/agencies")
async def get_all_agencies():
    return conn.execute(ag.select()).fetchall()

@agencies.post("/agencies/create")
async def create_agency(new_agency: Agencies):
    new_agency = {
        "id": new_agency.id,
        "name": new_agency.name,
        "address": new_agency.address,
        "RFC": new_agency.address,
        "email": new_agency.email,
        "password": new_agency.password,
        "url": new_agency.url,
        "agency_code": new_agency.agency_code,
        "phone": new_agency.phone,
        "postal_code": new_agency.postal_code
    }

    result = conn.execute(ag.insert().values(new_agency))
    print(result.lastrowid)
    return conn.execute(ag.select().where(ag.c.id == result.lastrowid)).first()
    




