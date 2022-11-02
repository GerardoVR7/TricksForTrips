from fastapi import APIRouter, Response, HTTPException
from config.database import conn
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.users import Users
from models.users import users

users_router = APIRouter()

@users_router.get("/users")
async def get_all_users():
    return conn.execute(users.select()).fetchall()

@users_router.post("/users/new")
async def create_user(new_user : Users):
    new_user = {
        "id": new_user.id,
        "email": new_user.email,
        "password": new_user.password
    }
    result = conn.execute(users.insert().values(new_user))
    print(result.lastrowid)
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()