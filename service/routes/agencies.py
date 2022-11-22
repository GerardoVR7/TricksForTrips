
from fastapi import APIRouter, Response, HTTPException
from ..config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from ..schema.agencies import Agencies
from ..models.agencies import agencies as ag

agencies = APIRouter()

@agencies.get("/agencies")
async def get_all_agencies():
    return conn.execute(ag.select()).fetchall()

@agencies.get("/agencies/{id}")
async def search_by_city(id_city : int):
    res = conn.execute(ag.select().where(ag.c.id == id_city)).first()
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")
    return res

@agencies.post("/agencies/create")
async def create_agency(new_agency: Agencies):
    new_agency = {
        "id": new_agency.id,
        "id_city": new_agency.id_city,
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
    




