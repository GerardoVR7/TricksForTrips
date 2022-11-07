from fastapi import APIRouter, Response, HTTPException
from config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.restaurants import Restaurants
from models.restaurants import restaurants

restaurant_router = APIRouter()

@restaurant_router.get("/restaurants")
async def get_all_restaurants():
    return conn.execute(restaurants.select()).fetchall()

@restaurant_router.post("/restaurants/new")
async def create_reastaurant(new_restaurant: Restaurants):
    new_restaurant = {
        "id": new_restaurant.id,
        "name": new_restaurant.name,
        "description": new_restaurant.description,
        "address": new_restaurant.address,
        "RFC": new_restaurant.RFC,
        "email": new_restaurant.email,
        "password": new_restaurant.password,
        "url": new_restaurant.url,
        "cellphone": new_restaurant.cellphone,
        "postal_code": new_restaurant.postal_code
    }

    result = conn.execute(restaurants.insert().values(new_restaurant))
    print(result.lastrowid)
    return conn.execute(restaurants.select().where(restaurants.c.id == result.lastrowid)).first()
