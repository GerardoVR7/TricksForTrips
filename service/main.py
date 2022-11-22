
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.mexico_cities import mexico_cities_router
from .routes.activities import activities
from .routes.tours import tours
from .routes.tours_services import tours_services_router
from .routes.files_service import files_router

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
app.include_router(tours)
app.include_router(tours_services_router)
app.include_router(files_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
    