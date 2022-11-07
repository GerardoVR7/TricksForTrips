from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.restaurant import restaurant_router
from routes.type_dish import type_dish_router
from routes.menus import menus_router
from routes.dishes import dishes_router

app = FastAPI()

origins = [

    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(restaurant_router)
app.include_router(menus_router)
app.include_router(type_dish_router)
app.include_router(dishes_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
    