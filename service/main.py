import imp
from operator import imod
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.activities import activities
from .routes.agencies import agencies
from .routes.tours import tours
from .routes.restaurant import restaurant_router
from .routes.type_dish import type_dish_router
from .routes.menus import menus_router
from .routes.dishes import dishes_router
from .routes.tourist import tourist_router
from .routes.tours_services import tours_services_router
from .routes.mexico_cities import mexico_cities_router
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
app.include_router(mexico_cities_router)
app.include_router(activities)
app.include_router(agencies)
app.include_router(tours)
app.include_router(restaurant_router)
app.include_router(menus_router)
app.include_router(type_dish_router)
app.include_router(dishes_router)
app.include_router(tourist_router)
app.include_router(tours_services_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
    