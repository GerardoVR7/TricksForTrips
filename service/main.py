
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.bookings import booking_router
# from .routes.openpay import openpay_router
from .routes.paypal import payment_routes

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
app.include_router(booking_router)
app.include_router(payment_routes)
# app.include_router(openpay_router)

@app.get("/")
def read_root():
    return {"Programador message": "Aiuda esto es sobre explotacion laboral"}
    